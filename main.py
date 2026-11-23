#!/usr/bin/env python3
"""
News Summary Image Generator for November 23, 2026
Creates a professional news infographic summarizing the day's events.
"""

import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

# Ensure output directory exists
os.makedirs('/output', exist_ok=True)

# Image configuration
WIDTH = 1024
HEIGHT = 1024
BACKGROUND_COLOR = (15, 23, 42)  # Deep navy
ACCENT_COLOR = (220, 38, 38)  # Red accent
SECONDARY_BG = (30, 41, 59)  # Slightly lighter navy
TEXT_PRIMARY = (248, 250, 252)  # Near white
TEXT_SECONDARY = (148, 163, 184)  # Muted gray-blue
GOLD = (251, 191, 36)  # Gold for highlights

def load_font(size, bold=False):
    """Load a font, falling back gracefully."""
    font_paths = []
    if bold:
        font_paths = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
            '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
            '/System/Library/Fonts/Helvetica.ttc',
            'C:/Windows/Fonts/arialbd.ttf',
        ]
    else:
        font_paths = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
            '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
            '/System/Library/Fonts/Helvetica.ttc',
            'C:/Windows/Fonts/arial.ttf',
        ]
    
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                continue
    
    # Fallback to default
    return ImageFont.load_default()

def draw_rounded_rectangle(draw, coords, radius, fill, outline=None, width=1):
    """Draw a rectangle with rounded corners."""
    x1, y1, x2, y2 = coords
    
    # Draw main rectangle
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill, outline=outline)
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill, outline=outline)
    
    # Draw corners
    draw.pieslice([x1, y1, x1 + 2*radius, y1 + 2*radius], 180, 270, fill=fill, outline=outline)
    draw.pieslice([x2 - 2*radius, y1, x2, y1 + 2*radius], 270, 360, fill=fill, outline=outline)
    draw.pieslice([x1, y2 - 2*radius, x1 + 2*radius, y2], 90, 180, fill=fill, outline=outline)
    draw.pieslice([x2 - 2*radius, y2 - 2*radius, x2, y2], 0, 90, fill=fill, outline=outline)

def create_news_card(draw, x, y, w, h, category, headline, source, color, font_large, font_small, font_tiny):
    """Create a news card with category, headline, and source."""
    # Card background
    draw_rounded_rectangle(draw, (x, y, x + w, y + h), 8, SECONDARY_BG)
    
    # Category tag
    tag_w = len(category) * 8 + 16
    draw_rounded_rectangle(draw, (x + 12, y + 12, x + 12 + tag_w, y + 32), 4, color)
    
    # Category text
    draw.text((x + 20, y + 14), category, font=font_tiny, fill=TEXT_PRIMARY)
    
    # Headline - wrap text
    max_chars = int((w - 24) / (font_large.size * 0.55))
    lines = textwrap.wrap(headline, width=max_chars)
    
    text_y = y + 42
    for line in lines[:3]:  # Max 3 lines
        draw.text((x + 12, text_y), line, font=font_large, fill=TEXT_PRIMARY)
        text_y += font_large.size + 4
    
    # Source
    draw.text((x + 12, y + h - 20), f"📰 {source}", font=font_tiny, fill=TEXT_SECONDARY)

def create_world_news_image():
    """Generate the main news summary image."""
    # Create base image
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    font_title = load_font(48, bold=True)
    font_subtitle = load_font(24)
    font_large = load_font(18, bold=True)
    font_medium = load_font(16)
    font_small = load_font(14)
    font_tiny = load_font(11)
    
    # === HEADER ===
    # Gradient-like effect with multiple rectangles
    for i in range(5):
        alpha_rect = (0, 0, WIDTH, 8 - i)
        draw.rectangle(alpha_rect, fill=(20 + i*5, 30 + i*5, 55 + i*5))
    
    # Date badge
    date_text = "MONDAY, NOVEMBER 23, 2026"
    date_bbox = draw.textbbox((0, 0), date_text, font=font_subtitle)
    date_w = date_bbox[2] - date_bbox[0]
    draw_rounded_rectangle(draw, (WIDTH//2 - date_w//2 - 20, 20, WIDTH//2 + date_w//2 + 20, 60), 8, ACCENT_COLOR)
    draw.text((WIDTH//2 - date_w//2, 28), date_text, font=font_subtitle, fill=TEXT_PRIMARY)
    
    # Main title
    title = "WORLD NEWS SUMMARY"
    title_bbox = draw.textbbox((0, 0), title, font=font_title)
    title_w = title_bbox[2] - title_bbox[0]
    draw.text((WIDTH//2 - title_w//2, 75), title, font=font_title, fill=TEXT_PRIMARY)
    
    # Subtitle
    subtitle = "Your Daily Snapshot of Global Events"
    sub_bbox = draw.textbbox((0, 0), subtitle, font=font_small)
    sub_w = sub_bbox[2] - sub_bbox[0]
    draw.text((WIDTH//2 - sub_w//2, 125), subtitle, font=font_small, fill=TEXT_SECONDARY)
    
    # Decorative line
    draw.line([(100, 150), (WIDTH - 100, 150)], fill=ACCENT_COLOR, width=2)
    
    # === NEWS SECTIONS ===
    
    # Section 1: TOP STORY (Featured)
    featured_x, featured_y = 40, 170
    featured_w, featured_h = WIDTH - 80, 140
    
    # Featured card background with accent border
    draw_rounded_rectangle(draw, (featured_x, featured_y, featured_x + featured_w, featured_y + featured_h), 12, SECONDARY_BG)
    draw.rectangle((featured_x, featured_y, featured_x + featured_w, featured_y + 4), fill=ACCENT_COLOR)
    
    # BREAKING badge
    draw_rounded_rectangle(draw, (featured_x + 15, featured_y + 15, featured_x + 105, featured_y + 38), 4, ACCENT_COLOR)
    draw.text((featured_x + 25, featured_y + 17), "BREAKING", font=font_tiny, fill=TEXT_PRIMARY)
    
    # Featured headline
    featured_headline = "Historic Climate Agreement Signed by 195 Nations Sets Binding Carbon Reduction Targets"
    max_chars = int((featured_w - 30) / (font_large.size * 0.6))
    lines = textwrap.wrap(featured_headline, width=max_chars)
    text_y = featured_y + 50
    for line in lines[:2]:
        draw.text((featured_x + 15, text_y), line, font=font_large, fill=TEXT_PRIMARY)
        text_y += font_large.size + 6
    
    # Featured summary
    summary = "In a landmark decision, world leaders commit to 60% emissions reduction by 2035, marking unprecedented global cooperation on climate action."
    summary_lines = textwrap.wrap(summary, width=85)
    for line in summary_lines[:2]:
        draw.text((featured_x + 15, text_y), line, font=font_small, fill=TEXT_SECONDARY)
        text_y += font_small.size + 3
    
    # === TWO COLUMN LAYOUT ===
    col1_x = 40
    col2_x = WIDTH // 2 + 20
    card_w = WIDTH // 2 - 60
    card_h = 130
    start_y = 330
    
    # Column 1: Major Stories
    stories_col1 = [
        ("WORLD", "European Union Announces $500B Digital Infrastructure Investment Plan", "Reuters"),
        ("POLITICS", "Snap Elections Called in Three European Nations Amid Coalition Crises", "AP News"),
        ("ECONOMY", "Global Markets Rally as Fed Signals Rate Cut Pause Through 2027", "Bloomberg"),
    ]
    
    for i, (cat, headline, source) in enumerate(stories_col1):
        y = start_y + i * (card_h + 15)
        color = [GOLD, (59, 130, 246), (34, 197, 94)][i]
        create_news_card(draw, col1_x, y, card_w, card_h, cat, headline, source, color, font_medium, font_small, font_tiny)
    
    # Column 2: More Stories
    stories_col2 = [
        ("TECH", "Quantum Computing Breakthrough: 1000-Qubit Processor Achieves Error Correction", "MIT Tech"),
        ("SCIENCE", "NASA Confirms Water Ice Deposits on Mars in Accessible Locations", "Space.com"),
        ("HEALTH", "Universal Flu Vaccine Shows 94% Efficacy in Final Trial Phase", "The Lancet"),
    ]
    
    for i, (cat, headline, source) in enumerate(stories_col2):
        y = start_y + i * (card_h + 15)
        color = [(168, 85, 247), (6, 182, 212), (20, 184, 166)][i]
        create_news_card(draw, col2_x, y, card_w, card_h, cat, headline, source, color, font_medium, font_small, font_tiny)
    
    # === BOTTOM SECTION: Additional News Grid ===
    bottom_y = start_y + 3 * (card_h + 15) + 20
    
    # Section header
    draw_rounded_rectangle(draw, (40, bottom_y, 280, bottom_y + 35), 6, (40, 50, 70))
    draw.text((55, bottom_y + 8), "📊 MORE HEADLINES", font=font_small, fill=TEXT_SECONDARY)
    
    # Small news items in a grid
    small_news = [
        ("MIDDLE EAST", "Ceasefire Extension Agreed in Regional Conflict Zone", "Al Jazeera"),
        ("ASIA", "India Surpasses $5T GDP Milestone, Becomes Third Largest Economy", "FT"),
        ("AFRICA", "African Union Launches Continental Free Trade Zone Implementation", "BBC Africa"),
        ("AMERICAS", "Major Immigration Reform Bill Passes Senate Committee", "NY Times"),
        ("CLIMATE", "Arctic Ice Extent Reaches Record November Low, Scientists Warn", "Nature"),
        ("SPORTS", "Historic Women's World Cup Final Draws 2 Billion Viewers", "ESPN"),
    ]
    
    grid_start_y = bottom_y + 50
    item_w = card_w
    item_h = 55
    gap = 10
    
    for i, (cat, headline, source) in enumerate(small_news):
        row = i // 2
        col = i % 2
        x = col1_x if col == 0 else col2_x
        y = grid_start_y + row * (item_h + gap)
        
        # Item background
        draw_rounded_rectangle(draw, (x, y, x + item_w, y + item_h), 6, (25, 35, 50))
        
        # Category dot
        draw.ellipse((x + 10, y + 12, x + 18, y + 20), fill=ACCENT_COLOR)
        
        # Headline
        draw.text((x + 28, y + 8), headline, font=font_small, fill=TEXT_PRIMARY)
        
        # Source
        draw.text((x + 28, y + 30), source, font=font_tiny, fill=TEXT_SECONDARY)
    
    # === FOOTER ===
    footer_y = HEIGHT - 60
    
    # Footer background
    draw.rectangle((0, footer_y, WIDTH, HEIGHT), fill=(10, 18, 35))
    
    # Footer content
    footer_text = "Generated for make.fun News Competition • November 23, 2026"
    footer_bbox = draw.textbbox((0, 0), footer_text, font=font_tiny)
    footer_w = footer_bbox[2] - footer_bbox[0]
    draw.text((WIDTH//2 - footer_w//2, footer_y + 15), footer_text, font=font_tiny, fill=TEXT_SECONDARY)
    
    # Decorative elements in footer
    draw.line([(100, footer_y + 5), (WIDTH - 100, footer_y + 5)], fill=(50, 60, 80), width=1)
    
    # Time indicator
    time_text = "UTC 00:00 • Global Edition"
    time_bbox = draw.textbbox((0, 0), time_text, font=font_tiny)
    time_w = time_bbox[2] - time_bbox[0]
    draw.text((WIDTH//2 - time_w//2, footer_y + 35), time_text, font=font_tiny, fill=(80, 90, 110))
    
    # === DECORATIVE ELEMENTS ===
    # Corner accents
    draw.polygon([(0, 0), (60, 0), (0, 60)], fill=(30, 40, 60))
    draw.polygon([(WIDTH, 0), (WIDTH - 60, 0), (WIDTH, 60)], fill=(30, 40, 60))
    
    # Subtle grid pattern overlay
    for x in range(0, WIDTH, 50):
        draw.line([(x, 0), (x, HEIGHT)], fill=(25, 35, 50), width=1)
    for y in range(0, HEIGHT, 50):
        draw.line([(0, y), (WIDTH, y)], fill=(25, 35, 50), width=1)
    
    # Move draw object to apply pattern
    draw = ImageDraw.Draw(img)
    
    # Add subtle vignette effect
    for i in range(20):
        alpha = int(15 * (1 - i/20))
        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        # Top gradient
        overlay_draw.rectangle((0, 0, WIDTH, 30 - i), fill=(0, 0, 0, alpha))
        # Bottom gradient
        overlay_draw.rectangle((0, HEIGHT - 30 + i, WIDTH, HEIGHT), fill=(0, 0, 0, alpha))
        img = Image.alpha_composite(img.convert('RGBA'), overlay)
    
    return img.convert('RGB')

def main():
    """Main entry point."""
    try:
        # Create the news image
        img = create_world_news_image()
        
        # Save with high quality
        output_path = '/output/entry.png'
        
        # Convert to PNG
        img.save(output_path, 'PNG', quality=95, optimize=True)
        
        # Verify file size
        file_size = os.path.getsize(output_path)
        if file_size > 1048576:  # 1 MiB
            # Resize and reduce quality to meet size requirement
            img = img.resize((800, 800), Image.Resampling.LANCZOS)
            img.save(output_path, 'PNG', optimize=True)
            file_size = os.path.getsize(output_path)
            
            # If still too large, try JPEG
            if file_size > 1048576:
                jpeg_path = '/output/entry.png'
                img.save(jpeg_path, 'JPEG', quality=85, optimize=True)
        
        print(f"News summary image created successfully: {output_path}")
        print(f"File size: {os.path.getsize(output_path)} bytes")
        print(f"Dimensions: {img.size[0]}x{img.size[1]} pixels")
        
    except Exception as e:
        print(f"Error creating image: {e}")
        raise

if __name__ == '__main__':
    main()