# AI Media Project

This repository contains AI-generated video content organized by workflow stage.

## Directory Structure

```
videos/
 ├─ raw/          # Original generated output
 ├─ renders/      # Processed / improved versions
 └─ final/        # Polished version for viewing
```

## Usage

The `videos` directory is the primary storage for video assets.

**Example:**
```python
videos = ["77a3d58c-c8c9-42c9-a41f-6f6729bfb1fb.mp4"]
```

or

```json
{
  "videos": ["grok-video-be3bac9c-6998-44c5-ab72-b83e8e8e379b.mp4"]
}
```

## Workflow

1. **Raw** → Store original generated video outputs
2. **Renders** → Process and improve videos
3. **Final** → Polished versions ready for viewing

## Automated Processing

This repository uses GitHub Actions to automatically process videos on every push to the main branch.

**Workflow steps:**
1. Checkout repository
2. Install FFmpeg and Python dependencies
3. Process videos using FFmpeg (scale to 720p, compress, etc.)
4. Commit and push processed videos

**To trigger processing:**
- Push to the `main` branch
- The workflow will automatically process videos and commit the results

**Manual processing:**
```bash
# Simple processing (copy only)
python3 scripts/process_videos.py

# FFmpeg processing (requires FFmpeg)
python3 scripts/process_with_ffmpeg.py
```
