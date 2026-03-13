# AI Media Project

> [!NOTE]
> This repository contains AI-generated video content organized by workflow stage.

## Summary

> [!IMPORTANT]
> The GitHub Actions workflow is now fully configured and working. Here's what's been set up:

<details>
<summary><b>Repository Structure</b></summary>

```
videos/
 ├─ raw/          # Original generated output (3 MP4 files)
 ├─ renders/      # Processed videos (3 MP4 files)
 └─ final/        # Final processed videos (3 MP4 files)
```

</details>

<details>
<summary><b>GitHub Actions Workflow</b> (<code>.github/workflows/process-videos.yml</code>)</summary>

- **Trigger**: Runs on every push to `main` branch
- **Permissions**: Has write access to commit processed videos
- **Steps**:
  1. Checkout repository with Git LFS support
  2. Install FFmpeg and Python dependencies
  3. Process videos using FFmpeg (scale to 720p, compress, etc.)
  4. Upload processed videos to Git LFS
  5. Commit and push changes

</details>

<details>
<summary><b>Git LFS Configuration</b></summary>

- All MP4 files are tracked with Git LFS
- Videos are stored efficiently on GitHub's LFS servers
- LFS objects are automatically uploaded during workflow execution

</details>

<details>
<summary><b>Branch Protection</b></summary>

- **Main branch** is protected with the following rules:
  - Requires pull request reviews (1 approval)
  - Requires status checks to pass (`process-videos` workflow)
  - Enforces linear history
  - Prevents force pushes
  - Administrators are also enforced

</details>

<details>
<summary><b>Manual Processing Scripts</b></summary>

- `scripts/process_videos.py` - Simple copy processing
- `scripts/process_with_ffmpeg.py` - FFmpeg-based processing

</details>

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

> [!TIP]
> This repository uses GitHub Actions to automatically process videos on every push to the main branch.

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

## Branch Protection Configuration

> [!WARNING]
> This repository includes a `branch-protection.json` file that defines the branch protection rules for the `main` branch.

**Configuration file:** `branch-protection.json`

**Current rules:**
- Requires pull request reviews (1 approval)
- Requires status checks to pass (`process-videos` workflow)
- Enforces linear history (no merge commits)
- Prevents force pushes
- Enforces rules on administrators
