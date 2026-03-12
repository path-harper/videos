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
videos = ["demo.mp4"]
```

or

```json
{
  "videos": ["grok-imagen-demo.mp4"]
}
```

If the array specifically stores **generated outputs**, **`renders`** is a commonly used alternative in AI/media generation projects.

✅ **Final pick:** `videos`
