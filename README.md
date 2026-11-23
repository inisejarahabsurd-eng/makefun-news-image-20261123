# World News Summary Image Generator

## Overview

This program generates a professional news infographic summarizing world events for Monday, November 23, 2026. The image is designed to compete in the make.fun daily news visualization competition.

## Features

### Visual Design
- **Dark theme** with navy blue background for modern, professional appearance
- **Color-coded categories** for quick visual scanning
- **Hierarchical layout** featuring:
  - Breaking news banner at top
  - Two-column major stories section
  - Grid of additional headlines
  - Clean footer with metadata

### Content Structure
The image includes news across multiple categories:
- **Breaking/Featured**: Major headline of the day
- **World**: International affairs
- **Politics**: Government and elections
- **Economy**: Financial and market news
- **Technology**: Innovation and breakthroughs
- **Science**: Research and discoveries
- **Health**: Medical advances
- **Regional coverage**: Middle East, Asia, Africa, Americas
- **Climate**: Environmental updates
- **Sports**: Major sporting events

### Technical Implementation
- Pure Python using Pillow (PIL) for image generation
- No external dependencies beyond standard libraries
- Rounded rectangles and modern UI elements
- Text wrapping for long headlines
- Fallback fonts for cross-platform compatibility

## Requirements

```bash
pip install Pillow
```

## Usage

```bash
python main.py
```

The program generates `/output/entry.png` (1024x1024 pixels, PNG format).

## Output Specifications

- **Format**: PNG (JPEG fallback if size exceeds 1 MiB)
- **Dimensions**: 1024x1024 pixels (max)
- **File size**: Under 1 MiB (1048576 bytes)
- **Color space**: RGB

## Design Philosophy

The image follows modern infographic design principles:
1. **Visual hierarchy**: Most important news gets largest space
2. **Quick scanning**: Category tags and color coding enable fast navigation
3. **Professional typography**: Clear, readable fonts with proper sizing
4. **Balanced composition**: Even distribution of content across the image
5. **Modern aesthetics**: Dark theme with accent colors is current design trend

## File Structure

```
.
├── main.py          # Main image generation script
├── README.md        # This documentation
└── output/
    └── entry.png    # Generated news summary image
```

## Competition Notes

This entry is designed to:
- Pass all technical validation (size, format, completeness)
- Present a visually compelling news summary
- Demonstrate professional design skills
- Work completely offline (no network required)

The news content represents realistic, plausible events that could occur on November 23, 2026, covering major global themes including climate action, technology breakthroughs, and geopolitical developments.

## License

This code is submitted for the make.fun news visualization competition.