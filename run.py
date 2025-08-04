#!/usr/bin/env python3
"""
CLI script for capture_stream.

This script loads configuration, resolves the stream/video path,
and calls the appropriate capture function based on the source type.
"""

import sys
import argparse
import traceback
from utils.config_loader import load_config
from twitch_capture import get_twitch_stream_url
from capture_loop import capture_frames_from_stream, capture_frames_from_video


def resolve_source_path(config: dict) -> str:
    """
    Resolve the source path based on configuration.
    
    Args:
        config: Configuration dictionary
        
    Returns:
        The resolved source path (stream URL or video file path)
        
    Raises:
        ValueError: If source type is invalid or required fields are missing
    """
    stream_config = config.get("stream", {})
    source_type = stream_config.get("source_type")
    
    if source_type == "twitch":
        username = stream_config.get("twitch_username")
        if not username:
            raise ValueError("twitch_username is required when source_type is 'twitch'")
        
        try:
            return get_twitch_stream_url(username)
        except Exception as e:
            raise ValueError(f"Failed to get Twitch stream URL for {username}: {e}")
    
    elif source_type == "video":
        video_path = stream_config.get("video_path")
        if not video_path:
            raise ValueError("video_path is required when source_type is 'video'")
        
        return video_path
    
    else:
        raise ValueError(f"Invalid source_type: {source_type}. Must be 'twitch' or 'video'")


def main():
    """Main entry point for the CLI script."""
    parser = argparse.ArgumentParser(
        description="Capture frames from Twitch streams or video files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run.py                    # Use default config.yaml
  python run.py -c my_config.yaml # Use custom config file
        """
    )
    
    parser.add_argument(
        "-c", "--config",
        default="config.yaml",
        help="Path to configuration file (default: config.yaml)"
    )
    
    args = parser.parse_args()
    
    try:
        # Load configuration
        print(f"Loading configuration from {args.config}...")
        config = load_config(args.config)
        
        # Resolve source path
        print("Resolving source path...")
        source_path = resolve_source_path(config)
        
        # Determine source type for logging
        source_type = config.get("stream", {}).get("source_type", "unknown")
        print(f"Source type: {source_type}")
        
        if source_type == "twitch":
            print(f"Capturing from Twitch stream: {source_path}")
            capture_frames_from_stream(source_path, config)
        else:
            print(f"Capturing from video file: {source_path}")
            capture_frames_from_video(source_path, config)
        
        print("Frame capture completed successfully!")
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nCapture interrupted by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        print(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main() 