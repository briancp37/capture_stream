from datetime import datetime, timezone


def generate_frame_filename(frame_index: int) -> str:
    """
    Generate a filename for a frame with UTC timestamp and zero-padded frame number.
    
    Args:
        frame_index: The frame number/index
        
    Returns:
        A string in format: frame_YYYYMMDD_HHMMSS_XXXXXX.jpg
        Example: frame_20250801_145301_000012.jpg
    """
    # Get current UTC timestamp
    now = datetime.now(timezone.utc)
    
    # Format timestamp as YYYYMMDD_HHMMSS
    timestamp = now.strftime('%Y%m%d_%H%M%S')
    
    # Format frame index as zero-padded 6-digit number
    frame_number = f"{frame_index:06d}"
    
    # Combine into filename
    filename = f"frame_{timestamp}_{frame_number}.jpg"
    
    return filename 