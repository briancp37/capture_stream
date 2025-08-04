import unittest
from unittest.mock import patch, MagicMock
import subprocess
from twitch_capture import get_twitch_stream_url


class TestTwitchCapture(unittest.TestCase):
    
    def test_get_twitch_stream_url_success(self):
        """Test successful stream URL retrieval"""
        mock_output = "https://example.com/stream.m3u8\n"
        
        with patch('subprocess.check_output') as mock_check_output:
            mock_check_output.return_value = mock_output
            
            result = get_twitch_stream_url("testuser")
            
            # Verify the function was called with correct arguments
            mock_check_output.assert_called_once_with(
                ["streamlink", "--stream-url", "https://twitch.tv/testuser", "best"],
                stderr=subprocess.STDOUT,
                text=True
            )
            
            # Verify the result
            self.assertEqual(result, "https://example.com/stream.m3u8")
    
    def test_get_twitch_stream_url_failure(self):
        """Test that subprocess failure raises an error"""
        with patch('subprocess.check_output') as mock_check_output:
            mock_check_output.side_effect = subprocess.CalledProcessError(
                returncode=1, 
                cmd=["streamlink", "--stream-url", "https://twitch.tv/testuser", "best"],
                output="Error: No streams found"
            )
            
            with self.assertRaises(subprocess.CalledProcessError):
                get_twitch_stream_url("testuser")
    
    def test_get_twitch_stream_url_strips_whitespace(self):
        """Test that whitespace is stripped from the output"""
        mock_output = "  https://example.com/stream.m3u8  \n"
        
        with patch('subprocess.check_output') as mock_check_output:
            mock_check_output.return_value = mock_output
            
            result = get_twitch_stream_url("testuser")
            
            self.assertEqual(result, "https://example.com/stream.m3u8")


if __name__ == '__main__':
    unittest.main() 