import unittest
from unittest.mock import Mock, patch, MagicMock
import tempfile
import os
import cv2
import numpy as np
from capture_loop import (
    capture_frames_from_stream,
    capture_frames_from_video,
    forward_frame
)


class TestCaptureLoop(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.temp_dir = tempfile.mkdtemp()
        self.config = {
            "capture": {
                "mode": "fps",
                "fps": 1,
                "every_k": 30,
                "save_frames": True,
                "forward_to_analysis": False,
                "log_metadata": True
            },
            "paths": {
                "output_dir": self.temp_dir
            }
        }
    
    def tearDown(self):
        """Clean up test fixtures"""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def test_forward_frame_stub(self):
        """Test that forward_frame is a stub function"""
        # Should not raise any exception
        forward_frame("test_frame.jpg")
    
    @patch('cv2.VideoCapture')
    def test_capture_frames_from_stream_fps_mode(self, mock_video_capture):
        """Test capture_frames_from_stream with fps mode"""
        # Mock the video capture
        mock_cap = Mock()
        mock_video_capture.return_value = mock_cap
        
        # Mock frame reading
        mock_cap.read.side_effect = [
            (True, np.zeros((480, 640, 3), dtype=np.uint8)),  # frame 1
            (True, np.zeros((480, 640, 3), dtype=np.uint8)),  # frame 2
            (True, np.zeros((480, 640, 3), dtype=np.uint8)),  # frame 3
            (False, None)    # end of stream
        ]
        # Mock FPS getter to return a numeric value
        mock_cap.get.side_effect = lambda prop: 30.0 if prop == cv2.CAP_PROP_FPS else 0
        
        # Test with fps mode
        config = self.config.copy()
        config["capture"]["mode"] = "fps"
        config["capture"]["fps"] = 1
        
        capture_frames_from_stream("test_stream_url", config)
        
        # Verify VideoCapture was called with stream URL
        mock_video_capture.assert_called_once_with("test_stream_url")
        
        # Verify capture was released
        mock_cap.release.assert_called_once()
    
    @patch('cv2.VideoCapture')
    def test_capture_frames_from_video_every_frame_mode(self, mock_video_capture):
        """Test capture_frames_from_video with every_frame mode"""
        # Mock the video capture
        mock_cap = Mock()
        mock_video_capture.return_value = mock_cap
        
        # Mock frame reading
        mock_cap.read.side_effect = [
            (True, np.zeros((480, 640, 3), dtype=np.uint8)),  # frame 1
            (True, np.zeros((480, 640, 3), dtype=np.uint8)),  # frame 2
            (False, None)    # end of video
        ]
        # Mock FPS getter to return a numeric value
        mock_cap.get.side_effect = lambda prop: 30.0 if prop == cv2.CAP_PROP_FPS else 0
        
        # Test with every_frame mode
        config = self.config.copy()
        config["capture"]["mode"] = "every_frame"
        
        capture_frames_from_video("test_video.mp4", config)
        
        # Verify VideoCapture was called with video path
        mock_video_capture.assert_called_once_with("test_video.mp4")
        
        # Verify capture was released
        mock_cap.release.assert_called_once()
    
    @patch('cv2.VideoCapture')
    def test_capture_frames_from_stream_every_k_mode(self, mock_video_capture):
        """Test capture_frames_from_stream with every_k mode"""
        # Mock the video capture
        mock_cap = Mock()
        mock_video_capture.return_value = mock_cap
        
        # Mock frame reading - simulate 10 frames
        mock_cap.read.side_effect = [(True, np.zeros((480, 640, 3), dtype=np.uint8)) for _ in range(10)] + [(False, None)]
        # Mock FPS getter to return a numeric value
        mock_cap.get.side_effect = lambda prop: 30.0 if prop == cv2.CAP_PROP_FPS else 0
        
        # Test with every_k mode
        config = self.config.copy()
        config["capture"]["mode"] = "every_k"
        config["capture"]["every_k"] = 3
        
        capture_frames_from_stream("test_stream_url", config)
        
        # Verify VideoCapture was called
        mock_video_capture.assert_called_once_with("test_stream_url")
        
        # Verify capture was released
        mock_cap.release.assert_called_once()
    
    @patch('cv2.VideoCapture')
    def test_capture_frames_save_frames_disabled(self, mock_video_capture):
        """Test that frames are not saved when save_frames is False"""
        # Mock the video capture
        mock_cap = Mock()
        mock_video_capture.return_value = mock_cap
        
        # Mock frame reading
        mock_cap.read.side_effect = [
            (True, np.zeros((480, 640, 3), dtype=np.uint8)),
            (False, None)
        ]
        # Mock FPS getter to return a numeric value
        mock_cap.get.side_effect = lambda prop: 30.0 if prop == cv2.CAP_PROP_FPS else 0
        
        # Test with save_frames disabled
        config = self.config.copy()
        config["capture"]["save_frames"] = False
        
        capture_frames_from_video("test_video.mp4", config)
        
        # Verify VideoCapture was called
        mock_video_capture.assert_called_once_with("test_video.mp4")
        
        # Verify capture was released
        mock_cap.release.assert_called_once()
    
    @patch('cv2.VideoCapture')
    def test_capture_frames_forward_to_analysis_enabled(self, mock_video_capture):
        """Test that forward_frame is called when forward_to_analysis is True"""
        # Mock the video capture
        mock_cap = Mock()
        mock_video_capture.return_value = mock_cap
        
        # Mock frame reading
        mock_cap.read.side_effect = [
            (True, np.zeros((480, 640, 3), dtype=np.uint8)),
            (False, None)
        ]
        # Mock FPS getter to return a numeric value
        mock_cap.get.side_effect = lambda prop: 30.0 if prop == cv2.CAP_PROP_FPS else 0
        
        # Test with forward_to_analysis enabled
        config = self.config.copy()
        config["capture"]["forward_to_analysis"] = True
        config["capture"]["mode"] = "every_frame"  # Ensure we save the frame
        
        with patch('capture_loop.forward_frame') as mock_forward:
            capture_frames_from_video("test_video.mp4", config)
            
            # Verify forward_frame was called
            mock_forward.assert_called()
    
    @patch('cv2.VideoCapture')
    def test_capture_frames_invalid_mode(self, mock_video_capture):
        """Test that invalid capture mode raises ValueError"""
        # Mock the video capture
        mock_cap = Mock()
        mock_video_capture.return_value = mock_cap
        
        # Mock frame reading
        mock_cap.read.side_effect = [
            (True, np.zeros((480, 640, 3), dtype=np.uint8)),
            (False, None)
        ]
        # Mock FPS getter to return a numeric value
        mock_cap.get.side_effect = lambda prop: 30.0 if prop == cv2.CAP_PROP_FPS else 0
        
        # Test with invalid mode
        config = self.config.copy()
        config["capture"]["mode"] = "invalid_mode"
        
        with self.assertRaises(ValueError):
            capture_frames_from_video("test_video.mp4", config)
    
    @patch('cv2.VideoCapture')
    def test_capture_frames_output_directory_creation(self, mock_video_capture):
        """Test that output directory is created if it doesn't exist"""
        # Mock the video capture
        mock_cap = Mock()
        mock_video_capture.return_value = mock_cap
        
        # Mock frame reading
        mock_cap.read.side_effect = [
            (True, np.zeros((480, 640, 3), dtype=np.uint8)),
            (False, None)
        ]
        # Mock FPS getter to return a numeric value
        mock_cap.get.side_effect = lambda prop: 30.0 if prop == cv2.CAP_PROP_FPS else 0
        
        # Test with non-existent output directory
        config = self.config.copy()
        config["paths"]["output_dir"] = os.path.join(self.temp_dir, "new_dir")
        
        capture_frames_from_video("test_video.mp4", config)
        
        # Verify directory was created
        self.assertTrue(os.path.exists(config["paths"]["output_dir"]))

    @patch('cv2.VideoCapture')
    def test_frame_logging_metadata(self, mock_video_capture):
        """Test that frame metadata is logged to CSV when log_metadata is True"""
        # Mock the video capture
        mock_cap = Mock()
        mock_video_capture.return_value = mock_cap
        
        # Mock frame reading - simulate 2 frames
        mock_cap.read.side_effect = [
            (True, np.zeros((480, 640, 3), dtype=np.uint8)),  # frame 1
            (True, np.zeros((720, 1280, 3), dtype=np.uint8)), # frame 2
            (False, None)    # end of stream
        ]
        # Mock FPS getter to return a numeric value
        mock_cap.get.side_effect = lambda prop: 30.0 if prop == cv2.CAP_PROP_FPS else 0
        
        # Test with log_metadata enabled and every_frame mode
        config = self.config.copy()
        config["capture"]["mode"] = "every_frame"
        config["capture"]["log_metadata"] = True
        config["stream"] = {"source_type": "twitch"}
        
        capture_frames_from_video("test_video.mp4", config)
        
        # Check that frame_log.csv was created in output_dir
        log_file_path = os.path.join(self.temp_dir, "frame_log.csv")
        self.assertTrue(os.path.exists(log_file_path))
        
        # Read and verify CSV content
        import csv
        with open(log_file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            
            # Should have 2 rows (one for each saved frame)
            self.assertEqual(len(rows), 2)
            
            # Check column names
            expected_columns = ['frame_index', 'timestamp', 'filename', 'source_type', 'resolution']
            self.assertEqual(list(rows[0].keys()), expected_columns)
            
            # Check first row data
            first_row = rows[0]
            self.assertEqual(first_row['frame_index'], '0')
            self.assertEqual(first_row['source_type'], 'twitch')
            self.assertEqual(first_row['resolution'], '640x480')
            self.assertTrue(first_row['filename'].startswith('frame_'))
            self.assertTrue(first_row['filename'].endswith('.jpg'))
            
            # Check second row data
            second_row = rows[1]
            self.assertEqual(second_row['frame_index'], '1')
            self.assertEqual(second_row['source_type'], 'twitch')
            self.assertEqual(second_row['resolution'], '1280x720')
            self.assertTrue(second_row['filename'].startswith('frame_'))
            self.assertTrue(second_row['filename'].endswith('.jpg'))

    @patch('cv2.VideoCapture')
    def test_frame_logging_disabled(self, mock_video_capture):
        """Test that frame metadata is not logged when log_metadata is False"""
        # Mock the video capture
        mock_cap = Mock()
        mock_video_capture.return_value = mock_cap
        
        # Mock frame reading
        mock_cap.read.side_effect = [
            (True, np.zeros((480, 640, 3), dtype=np.uint8)),
            (False, None)
        ]
        # Mock FPS getter to return a numeric value
        mock_cap.get.side_effect = lambda prop: 30.0 if prop == cv2.CAP_PROP_FPS else 0
        
        # Test with log_metadata disabled
        config = self.config.copy()
        config["capture"]["mode"] = "every_frame"
        config["capture"]["log_metadata"] = False
        
        capture_frames_from_video("test_video.mp4", config)
        
        # Check that frame_log.csv was NOT created
        log_file_path = os.path.join(self.temp_dir, "frame_log.csv")
        self.assertFalse(os.path.exists(log_file_path))


if __name__ == '__main__':
    unittest.main() 