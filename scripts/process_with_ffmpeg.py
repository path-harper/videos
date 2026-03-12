#!/usr/bin/env python3
"""
Advanced Video Processing Pipeline with FFmpeg
This script processes videos from the raw directory using FFmpeg.
"""

import os
import subprocess
import shutil
from pathlib import Path

# Configuration
RAW_DIR = Path("videos/raw")
RENDERS_DIR = Path("videos/renders")
FINAL_DIR = Path("videos/final")

def create_directories():
    """Create necessary directories if they don't exist."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    RENDERS_DIR.mkdir(parents=True, exist_ok=True)
    FINAL_DIR.mkdir(parents=True, exist_ok=True)

def check_ffmpeg():
    """Check if FFmpeg is installed."""
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def process_video_with_ffmpeg(input_path, output_path, preset="medium"):
    """
    Process a video using FFmpeg.
    
    Args:
        input_path: Path to input video
        output_path: Path to output video
        preset: FFmpeg preset (ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow)
    """
    print(f"  Processing: {input_path.name}")

    # Basic FFmpeg command with some processing
    cmd = [
        "ffmpeg",
        "-i", str(input_path),
        "-vf", "scale=1280:720",  # Scale to 720p
        "-c:v", "libx264",
        "-preset", preset,
        "-crf", "23",
        "-c:a", "aac",
        "-b:a", "192k",
        "-y",  # Overwrite output file
        str(output_path)
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"    Error processing {input_path.name}: {e}")
        return False

def copy_to_renders():
    """Copy videos from raw to renders directory."""
    print("Copying videos from raw to renders...")
    for video_file in RAW_DIR.glob("*.mp4"):
        destination = RENDERS_DIR / video_file.name
        shutil.copy2(video_file, destination)
        print(f"  Copied: {video_file.name}")

def process_videos():
    """Process videos using FFmpeg."""
    print("\nProcessing videos with FFmpeg...")
    processed_count = 0

    for video_file in RENDERS_DIR.glob("*.mp4"):
        output_file = FINAL_DIR / video_file.name
        if process_video_with_ffmpeg(video_file, output_file):
            processed_count += 1

    return processed_count

def main():
    """Main processing pipeline."""
    print("=== Video Processing Pipeline with FFmpeg ===\n")

    # Check FFmpeg
    if not check_ffmpeg():
        print("FFmpeg not found. Please install FFmpeg to use this script.")
        print("Installation instructions:")
        print("  macOS: brew install ffmpeg")
        print("  Ubuntu: sudo apt install ffmpeg")
        print("  Windows: Download from https://ffmpeg.org/download.html")
        print("\nFalling back to simple copy mode.\n")
        # Fall back to simple processing
        create_directories()
        copy_to_renders()
        for video_file in RENDERS_DIR.glob("*.mp4"):
            shutil.copy2(video_file, FINAL_DIR / video_file.name)
        print("\n=== Processing Complete (Copy Mode) ===")
        return

    # Create directories
    create_directories()
    print("Directories created/verified.\n")

    # Copy raw to renders
    copy_to_renders()

    # Process videos
    processed_count = process_videos()

    print(f"\n=== Processing Complete ===")
    print(f"Processed {processed_count} videos")
    print(f"\nVideo locations:")
    print(f"  Raw: {RAW_DIR}")
    print(f"  Renders: {RENDERS_DIR}")
    print(f"  Final: {FINAL_DIR}")

if __name__ == "__main__":
    main()
