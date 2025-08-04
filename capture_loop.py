import cv2
import os
import numpy as np
from utils.frame_namer import generate_frame_filename
from utils.path_utils import ensure_dir


def _compute_frame_hash(frame: np.ndarray) -> str:
    """
    Compute a fast perceptual hash (dHash) for duplicate frame detection.
    
    This uses a difference hash which is:
    - Fast to compute (works well on Jetson Orin Nano)
    - Memory efficient (64-bit hash)
    - Robust to minor compression artifacts
    - Cross-platform compatible
    
    Args:
        frame: OpenCV frame as numpy array
        
    Returns:
        String representation of 64-bit hash
    """
    # Resize to 9x8 for dHash (8x8 differences)
    resized = cv2.resize(frame, (9, 8))
    
    # Convert to grayscale if needed
    if len(resized.shape) == 3:
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    else:
        gray = resized
    
    # Compute differences between adjacent pixels
    diff = gray[:, 1:] > gray[:, :-1]
    
    # Convert to 64-bit hash
    hash_value = 0
    for i, row in enumerate(diff):
        for j, pixel in enumerate(row):
            if pixel:
                hash_value |= 1 << (i * 8 + j)
    
    return f"{hash_value:016x}"  # Return as hex string


def _is_duplicate_frame(frame: np.ndarray, seen_hashes: set, hash_threshold: int = 0) -> bool:
    """
    Check if frame is a duplicate using perceptual hashing.
    
    Args:
        frame: OpenCV frame as numpy array
        seen_hashes: Set of previously seen frame hashes
        hash_threshold: Hamming distance threshold for considering frames similar (0 = exact match)
        
    Returns:
        True if frame is considered a duplicate, False otherwise
    """
    frame_hash = _compute_frame_hash(frame)
    
    if hash_threshold == 0:
        # Exact match - fastest for most cases
        return frame_hash in seen_hashes
    
    # For non-zero threshold, check Hamming distance
    for seen_hash in seen_hashes:
        # Convert hex strings to integers for bitwise operations
        hash1 = int(frame_hash, 16)
        hash2 = int(seen_hash, 16)
        
        # Compute Hamming distance
        distance = bin(hash1 ^ hash2).count('1')
        
        if distance <= hash_threshold:
            return True
    
    return False


def forward_frame(frame_path: str):
    """Stub function for forwarding frames to analysis pipeline."""
    pass  # stub for now


def capture_frames_from_stream(stream_url: str, config: dict):
    """
    Capture frames from a stream URL using OpenCV.
    
    Args:
        stream_url: URL of the stream to capture from
        config: Configuration dictionary containing capture settings
    """
    _capture_frames(stream_url, config, is_stream=True)


def capture_frames_from_video(video_path: str, config: dict):
    """
    Capture frames from a video file using OpenCV.
    
    Args:
        video_path: Path to the video file to capture from
        config: Configuration dictionary containing capture settings
    """
    _capture_frames(video_path, config, is_stream=False)


def _capture_frames(source: str, config: dict, is_stream: bool):
    """
    Internal function to capture frames from either a stream or video file.
    
    Args:
        source: Stream URL or video file path
        config: Configuration dictionary containing capture settings
        is_stream: True if capturing from stream, False if from video file
    """
    # Ensure output directory exists
    output_dir = config["paths"]["output_dir"]
    ensure_dir(output_dir)
    
    # Get capture settings
    capture_config = config["capture"]
    mode = capture_config["mode"]
    save_frames = capture_config.get("save_frames", True)
    forward_to_analysis = capture_config.get("forward_to_analysis", False)
    log_metadata = capture_config.get("log_metadata", False)
    
    # Duplicate detection settings
    skip_duplicates = capture_config.get("skip_duplicates", True)
    hash_threshold = capture_config.get("hash_threshold", 0)  # 0 = exact match, higher = more lenient
    seen_hashes = set()  # Track seen frame hashes
    
    # Initialize video capture
    cap = cv2.VideoCapture(source)
    
    if not cap.isOpened():
        raise ValueError(f"Failed to open video source: {source}")
    
    try:
        # Get source FPS for timing calculations
        source_fps = cap.get(cv2.CAP_PROP_FPS)
        if source_fps <= 0:
            source_fps = 30.0  # Default fallback
        
        frame_count = 0
        saved_count = 0
        
        # Calculate frame intervals based on mode
        if mode == "fps":
            target_fps = capture_config.get("fps", 1)
            frame_interval = max(1, int(source_fps / target_fps))
        elif mode == "every_k":
            frame_interval = capture_config.get("every_k", 30)
        elif mode == "every_frame":
            frame_interval = 1
        else:
            raise ValueError(f"Invalid capture mode: {mode}")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_count += 1
            
            # Determine if we should save this frame
            should_save = False
            if mode == "every_frame":
                should_save = True
            elif mode == "fps" or mode == "every_k":
                should_save = (frame_count % frame_interval == 0)
            
            if should_save and save_frames:
                # Check for duplicates if enabled
                is_duplicate = False
                if skip_duplicates:
                    is_duplicate = _is_duplicate_frame(frame, seen_hashes, hash_threshold)
                
                if not is_duplicate:
                    # Generate filename and save frame
                    filename = generate_frame_filename(saved_count)
                    frame_path = os.path.join(output_dir, filename)
                    
                    success = cv2.imwrite(frame_path, frame)
                    if success:
                        saved_count += 1
                        
                        # Add frame hash to seen set
                        if skip_duplicates:
                            frame_hash = _compute_frame_hash(frame)
                            seen_hashes.add(frame_hash)
                        
                        # Log metadata if enabled
                        if log_metadata:
                            _log_frame_metadata(frame_path, frame_count, saved_count, config)
                        
                        # Forward frame if enabled
                        if forward_to_analysis:
                            forward_frame(frame_path)
        
        print(f"Captured {saved_count} frames from {frame_count} total frames")
        
    finally:
        cap.release()


def _log_frame_metadata(frame_path: str, frame_count: int, saved_count: int, config: dict):
    """
    Log metadata about a saved frame to CSV file.
    
    Args:
        frame_path: Path to the saved frame
        frame_count: Current frame number in the source
        saved_count: Number of frames saved so far
        config: Configuration dictionary
    """
    import csv
    import os
    from datetime import datetime, timezone
    
    # Place frame_log.csv in output_dir
    output_dir = config["paths"]["output_dir"]
    log_file = os.path.join(output_dir, "frame_log.csv")
    file_exists = os.path.exists(log_file)
    
    # Get frame resolution from the saved image
    frame = cv2.imread(frame_path)
    if frame is not None:
        height, width = frame.shape[:2]
        resolution = f"{width}x{height}"
    else:
        resolution = "unknown"
    
    # Get filename from frame_path
    filename = os.path.basename(frame_path)
    
    # Get source type from config
    source_type = config.get('stream', {}).get('source_type', 'unknown')
    
    with open(log_file, 'a', newline='') as csvfile:
        fieldnames = ['frame_index', 'timestamp', 'filename', 'source_type', 'resolution']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow({
            'frame_index': str(saved_count - 1),  # Use 0-based index
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'filename': filename,
            'source_type': source_type,
            'resolution': resolution
        }) 