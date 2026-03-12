# AI Media Project

This repository contains AI-generated video content.

## Directory Structure

```
videos/
 ├─ raw/          # Original generated output
 ├─ renders/      # Processed / improved versions
 └─ final/        # Polished version for viewing
```

## Usage

The `videos` directory is the primary storage for video assets.

```python
videos = ["77a3d58c-c8c9-42c9-a41f-6f6729bfb1fb.mp4"]
```

or

```json
{
  "videos": ["grok-video-be3bac9c-6998-44c5-ab72-b83e8e8e379b.mp4"]
}
```

If the array specifically stores **generated outputs**, **`renders`** is a commonly used alternative in AI/media generation projects.

✅ **Final pick:** `videos`
