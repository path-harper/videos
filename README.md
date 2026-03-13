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
> This repository includes a [`branch-protection.json`](branch-protection.json) file that defines the branch protection rules for the `main` branch.

**Configuration file:** [`branch-protection.json`](branch-protection.json)

**Current rules:**

| Setting | Value | Description |
|---------|-------|-------------|
| `required_status_checks.strict` | `true` | Status checks must pass before merging |
| `required_status_checks.contexts` | `["process-videos"]` | Required workflow: [`process-videos`](.github/workflows/process-videos.yml) |
| `enforce_admins.enabled` | `true` | Rules apply to administrators too |
| `required_pull_request_reviews.required_approving_review_count` | `1` | Requires 1 approving review |
| `required_pull_request_reviews.dismiss_stale_reviews` | `false` | Stale reviews are not dismissed |
| `required_pull_request_reviews.require_code_owner_reviews` | `false` | Code owner reviews not required |
| `required_pull_request_reviews.require_last_push_approval` | `false` | Last push approval not required |
| `required_linear_history.enabled` | `true` | Enforces linear history (no merge commits) |
| `allow_force_pushes.enabled` | `false` | Prevents force pushes |
| `allow_deletions.enabled` | `false` | Prevents branch deletion |
| `block_creations.enabled` | `false` | Blocks branch creation |
| `required_conversation_resolution.enabled` | `false` | Requires conversation resolution |
| `lock_branch.enabled` | `false` | Locks branch (no direct pushes) |
| `allow_fork_syncing.enabled` | `false` | Disallows fork syncing |
| `required_signatures.enabled` | `false` | Requires signed commits (disabled)

### Merge Rules

> [!TIP]
> The `required_linear_history` rule affects how pull requests can be merged.

| Allowed Merge Methods | Blocked Merge Methods |
|----------------------|----------------------|
| ✅ Squash and merge | ❌ Create a merge commit |
| ✅ Rebase and merge | |

**Why?** The `required_linear_history.enabled = true` setting prevents merge commits to maintain a clean, linear Git history.

## Forking Rules

> [!NOTE]
> This repository has specific rules for forking and contributing.

### Forking the Repository

1. **Fork** the repository to your GitHub account
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/videos.git
   cd videos
   ```
3. **Add** the upstream repository:
   ```bash
   git remote add upstream https://github.com/path-harper/videos.git
   ```

### Contributing from a Fork

1. Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature
   ```

2. Make your changes and commit them

3. Push to your fork:
   ```bash
   git push origin feature/your-feature
   ```

4. Create a pull request from your fork to the upstream `main` branch

### Important Notes

- All pull requests must pass the `process-videos` workflow
- Requires 1 approving review from a collaborator
- Maintains linear history (no merge commits)
- [Git LFS](#git-lfs) is used for video files - ensure they are tracked properly

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

