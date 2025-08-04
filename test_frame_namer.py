import unittest
from datetime import datetime, timezone
import re
from utils.frame_namer import generate_frame_filename


class TestFrameNamer(unittest.TestCase):
    
    def test_generate_frame_filename_format(self):
        """Test that generate_frame_filename returns the correct format"""
        frame_index = 12
        filename = generate_frame_filename(frame_index)
        
        # Check the pattern: frame_YYYYMMDD_HHMMSS_XXXXXX.jpg
        pattern = r'^frame_\d{8}_\d{6}_\d{6}\.jpg$'
        self.assertIsNotNone(re.match(pattern, filename), 
                           f"Filename {filename} doesn't match expected pattern")
    
    def test_generate_frame_filename_frame_number(self):
        """Test that the frame number is correctly zero-padded"""
        frame_index = 12
        filename = generate_frame_filename(frame_index)
        
        # Extract the frame number part (last 6 digits before .jpg)
        frame_number_part = filename.split('_')[-1].replace('.jpg', '')
        self.assertEqual(frame_number_part, '000012')
    
    def test_generate_frame_filename_different_indices(self):
        """Test that different frame indices produce different filenames"""
        filename1 = generate_frame_filename(1)
        filename2 = generate_frame_filename(100)
        
        self.assertNotEqual(filename1, filename2)
        
        # Check that frame numbers are correctly padded
        frame_num1 = filename1.split('_')[-1].replace('.jpg', '')
        frame_num2 = filename2.split('_')[-1].replace('.jpg', '')
        
        self.assertEqual(frame_num1, '000001')
        self.assertEqual(frame_num2, '000100')
    
    def test_generate_frame_filename_timestamp_format(self):
        """Test that the timestamp is in UTC and correct format"""
        frame_index = 0
        filename = generate_frame_filename(frame_index)
        
        # Extract timestamp part (YYYYMMDD_HHMMSS)
        timestamp_part = '_'.join(filename.split('_')[1:3])
        
                # Verify it's a valid datetime
        try:
            parsed_time = datetime.strptime(timestamp_part, '%Y%m%d_%H%M%S')
            # Make parsed_time timezone-aware (UTC) for comparison
            parsed_time = parsed_time.replace(tzinfo=timezone.utc)
            # Should be recent (within last minute)
            now = datetime.now(timezone.utc)
            time_diff = abs((now - parsed_time).total_seconds())
            self.assertLess(time_diff, 60, "Timestamp should be recent UTC time")
        except ValueError:
            self.fail(f"Invalid timestamp format: {timestamp_part}")


if __name__ == '__main__':
    unittest.main() 