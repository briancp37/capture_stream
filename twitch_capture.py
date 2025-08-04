"""
Twitch stream capture utilities.

This module provides functions to interact with Twitch streams,
including retrieving stream URLs using streamlink.
"""

import subprocess
from typing import Optional
import traceback
traceback

def get_twitch_stream_url(username: str) -> str:
    """
    Get the stream URL for a Twitch username using streamlink.
    
    Args:
        username: The Twitch username to get the stream URL for
        
    Returns:
        The .m3u8 stream URL
        
    Raises:
        subprocess.CalledProcessError: If streamlink fails to get the stream URL
    """
    try:
        # Call streamlink to get the stream URL
        result = subprocess.check_output(
            # ["streamlink", "--stream-url", f"https://twitch.tv/{username}", "best"],
            ["streamlink", "--stream-url", f"twitch.tv/{username}", "best", "-O"],
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Return the URL with whitespace stripped
        return result.strip()
        
    except subprocess.CalledProcessError as e:
        # Re-raise the error as specified in the requirements
        print(traceback.format_exc())
        raise e 
    
    except Exception as e:
        # Re-raise the error as specified in the requirements
        print(traceback.format_exc())
        raise e 