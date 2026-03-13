# AI Media Project

This repository contains AI-generated video content organized by workflow stage.

## Summary

The GitHub Actions workflow is now fully configured and working. Here's what's been set up:

### **Repository Structure**
```
videos/
 ├─ raw/          # Original generated output (3 MP4 files)
 ├─ renders/      # Processed videos (3 MP4 files)
 └─ final/        # Final processed videos (3 MP4 files)
```

### **GitHub Actions Workflow** (`.github/workflows/process-videos.yml`)
- **Trigger**: Runs on every push to `main` branch
- **Permissions**: Has write access to commit processed videos
- **Steps**:
  1. Checkout repository with Git LFS support
  2. Install FFmpeg and Python dependencies
  3. Process videos using FFmpeg (scale to 720p, compress, etc.)
  4. Upload processed videos to Git LFS
  5. Commit and push changes

### **Git LFS Configuration**
- All MP4 files are tracked with Git LFS
- Videos are stored efficiently on GitHub's LFS servers
- LFS objects are automatically uploaded during workflow execution

### **Branch Protection**
- **Main branch** is protected with the following rules:
  - Requires pull request reviews (1 approval)
  - Requires status checks to pass (process-videos workflow)
  - Enforces linear history
  - Prevents force pushes
  - Administrators are also enforced

### **Manual Processing Scripts**
- `scripts/process_videos.py` - Simple copy processing
- `scripts/process_with_ffmpeg.py` - FFmpeg-based processing

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

**To trigger processing:**
- Push to the `main` branch
- The workflow will automatically process videos and upload them to Git LFS

**Manual processing:**
```bash
# Simple processing (copy only)
python3 scripts/process_videos.py

# FFmpeg processing (requires FFmpeg)
python3 scripts/process_with_ffmpeg.py
```

## Git LFS

Videos are stored using Git LFS (Large File Storage) to handle large binary files efficiently.

**Setup Git LFS:**
```bash
git lfs install
git lfs track "videos/**/*.mp4"
```

**Pull videos from LFS:**
```bash
git lfs pull
```