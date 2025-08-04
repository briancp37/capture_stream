"""
Integration tests for twitch_capture module.

These tests require streamlink to be installed and may require internet connectivity.
"""

import unittest
import subprocess
from twitch_capture import get_twitch_stream_url


class TestTwitchCaptureIntegration(unittest.TestCase):
    
    def setUp(self):
        """Check if streamlink is available before running tests."""
        try:
            subprocess.run(["streamlink", "--version"], 
                         capture_output=True, check=True)
            self.streamlink_available = True
        except (subprocess.CalledProcessError, FileNotFoundError):
            self.streamlink_available = False
    
    def test_get_twitch_stream_url_integration(self):
        """Test with a real streamlink call (skipped if streamlink not available)."""
        if not self.streamlink_available:
            self.skipTest("streamlink not available")
        
        # Test with a known Twitch username (this will fail if not live)
        try:
            result = get_twitch_stream_url("test")
            # Should return a URL that contains .m3u8
            self.assertIn(".m3u8", result)
            self.assertTrue(result.startswith("http"))
        except subprocess.CalledProcessError:
            # This is expected if the user is not live
            pass
    
    def test_get_twitch_stream_url_invalid_user(self):
        """Test with an invalid username (should raise an error)."""
        if not self.streamlink_available:
            self.skipTest("streamlink not available")
        
        # Test with a clearly invalid username
        with self.assertRaises(subprocess.CalledProcessError):
            get_twitch_stream_url("this_is_definitely_not_a_real_twitch_username_12345")


if __name__ == '__main__':
    unittest.main() 