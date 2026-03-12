# Video Processing Scripts

This directory contains scripts for processing videos in the AI Media Project.

## Scripts

### 1. `process_videos.py` - Simple Processing
A basic script that copies videos from `raw` to `renders` to `final` without actual processing.

**Usage:**
```bash
python3 process_videos.py
```

### 2. `process_with_ffmpeg.py` - FFmpeg Processing
An advanced script that uses FFmpeg to process videos (scale to 720p, compress, etc.).

**Requirements:**
- FFmpeg must be installed on your system

**Installation:**
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

**Usage:**
```bash
python3 process_with_ffmpeg.py
```

## Video Workflow

1. **`videos/raw/`** - Store original generated video outputs
2. **`videos/renders/`** - Processed videos (intermediate step)
3. **`videos/final/`** - Final polished versions ready for viewing

## Processing Steps

The FFmpeg script performs the following operations:
- Scales video to 1280x720 (720p)
- Encodes with H.264 codec
- Uses medium preset for balance between speed and quality
- CRF 23 for good quality compression
- AAC audio at 192kbps

## Customization

You can customize the processing by modifying the FFmpeg parameters in `process_with_ffmpeg.py`:
- Change resolution: Modify the `-vf "scale=1280:720"` parameter
- Adjust quality: Change the `-crf` value (lower = better quality, 18-28 is typical)
- Change preset: Modify the `-preset` value for speed/quality trade-off
