#!/usr/bin/env python3
"""
WordPress to Jekyll Migration Script
=====================================
Converts a WordPress XML export into Jekyll-compatible Markdown posts.

Usage:
    1. Export your WordPress site:
       WordPress Admin -> Tools -> Export -> All Content -> Download Export File
    2. Place the XML file in this directory
    3. Run:  python3 migrate_wp.py your-export-file.xml

The script will:
  - Create markdown files in _posts/ with correct front matter
  - Convert HTML content to Markdown
  - Download and save images to assets/img/posts/
  - Preserve categories, tags, dates, and featured images
"""

import xml.etree.ElementTree as ET
import re
import os
import sys
import html
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

# WordPress export uses these namespaces
NAMESPACES = {
    'wp': 'http://wordpress.org/export/1.2/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
    'dc': 'http://purl.org/dc/elements/1.1/',
}


def slugify(text):
    """Convert text to URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def html_to_markdown(content):
    """Convert HTML content to Markdown (basic conversion)."""
    if not content:
        return ''

    text = content

    # Decode HTML entities
    text = html.unescape(text)

    # Convert headings
    for i in range(6, 0, -1):
        text = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', r'\n' + '#' * i + r' \1\n', text, flags=re.DOTALL)

    # Convert bold and italic
    text = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', text, flags=re.DOTALL)
    text = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', text, flags=re.DOTALL)

    # Convert links
    text = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.DOTALL)

    # Convert images
    text = re.sub(
        r'<img[^>]*src=["\']([^"\']*)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*/?>', r'![\2](\1)', text
    )
    text = re.sub(r'<img[^>]*src=["\']([^"\']*)["\'][^>]*/?>', r'![](\1)', text)

    # Convert lists
    text = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', text, flags=re.DOTALL)
    text = re.sub(r'</?[ou]l[^>]*>', '', text)

    # Convert blockquotes
    text = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', lambda m: '\n'.join(
        '> ' + line for line in m.group(1).strip().split('\n')
    ), text, flags=re.DOTALL)

    # Convert code blocks
    text = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', text, flags=re.DOTALL)
    text = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', text, flags=re.DOTALL)

    # Convert line breaks and paragraphs
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', text, flags=re.DOTALL)

    # Convert horizontal rules
    text = re.sub(r'<hr\s*/?>', '\n---\n', text)

    # WordPress specific: convert caption shortcodes
    text = re.sub(r'\[caption[^\]]*\](.*?)\[/caption\]', r'\1', text, flags=re.DOTALL)

    # WordPress specific: convert YouTube embeds
    text = re.sub(
        r'\[youtube[^\]]*\](https?://[^\[]*)\[/youtube\]',
        r'{% include embed/youtube.html id="\1" %}',
        text
    )

    # Strip remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Clean up whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()

    return text


def download_image(url, save_dir):
    """Download an image and return the local path."""
    try:
        filename = os.path.basename(url.split('?')[0])
        if not filename:
            return None
        local_path = os.path.join(save_dir, filename)
        if not os.path.exists(local_path):
            print(f"    Downloading: {filename}")
            urllib.request.urlretrieve(url, local_path)
        return f"/assets/img/posts/{filename}"
    except (urllib.error.URLError, Exception) as e:
        print(f"    Warning: Could not download {url}: {e}")
        return url  # Keep original URL if download fails


def process_images_in_content(content, img_dir):
    """Find image URLs in content and download them locally."""
    img_pattern = re.compile(r'!\[([^\]]*)\]\((https?://[^)]+)\)')

    def replace_image(match):
        alt_text = match.group(1)
        url = match.group(2)
        local_path = download_image(url, img_dir)
        return f'![{alt_text}]({local_path})'

    return img_pattern.sub(replace_image, content)


def parse_wordpress_export(xml_file):
    """Parse WordPress XML export and return list of posts."""
    print(f"Parsing {xml_file}...")
    tree = ET.parse(xml_file)
    root = tree.getroot()
    channel = root.find('channel')

    posts = []
    for item in channel.findall('item'):
        post_type = item.find('wp:post_type', NAMESPACES)
        status = item.find('wp:status', NAMESPACES)

        # Only process published posts and pages
        if post_type is None or post_type.text not in ('post', 'page'):
            continue
        if status is None or status.text != 'publish':
            continue

        title = item.find('title').text or 'Untitled'
        content_elem = item.find('content:encoded', NAMESPACES)
        content = content_elem.text if content_elem is not None and content_elem.text else ''

        pub_date_text = item.find('wp:post_date', NAMESPACES)
        if pub_date_text is not None and pub_date_text.text:
            try:
                pub_date = datetime.strptime(pub_date_text.text, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                pub_date = datetime.now()
        else:
            pub_date = datetime.now()

        # Get categories and tags
        categories = []
        tags = []
        for cat in item.findall('category'):
            domain = cat.get('domain', '')
            if domain == 'category':
                categories.append(cat.text)
            elif domain == 'post_tag':
                tags.append(cat.text)

        # Get featured image (if referenced in meta)
        # Note: WordPress exports don't always include this directly
        # The image will be in the content if it's there

        posts.append({
            'title': title,
            'content': content,
            'date': pub_date,
            'categories': categories,
            'tags': tags,
            'type': post_type.text,
            'slug': slugify(title),
        })

    print(f"Found {len(posts)} published items")
    return posts


def create_jekyll_post(post, output_dir, img_dir):
    """Create a Jekyll markdown file from a parsed post."""
    date_str = post['date'].strftime('%Y-%m-%d')
    filename = f"{date_str}-{post['slug']}.md"
    filepath = os.path.join(output_dir, filename)

    # Convert content
    markdown_content = html_to_markdown(post['content'])

    # Download and localize images
    markdown_content = process_images_in_content(markdown_content, img_dir)

    # Build front matter
    front_matter = '---\n'
    front_matter += f'title: "{post["title"]}"\n'
    front_matter += f'date: {post["date"].strftime("%Y-%m-%d %H:%M:%S")} +0530\n'

    if post['categories']:
        cats = ', '.join(post['categories'])
        front_matter += f'categories: [{cats}]\n'

    if post['tags']:
        tags = ', '.join(post['tags'])
        front_matter += f'tags: [{tags}]\n'

    front_matter += '---\n\n'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(front_matter + markdown_content)

    print(f"  Created: {filename}")
    return filename


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 migrate_wp.py <wordpress-export.xml>")
        print()
        print("To get the export file:")
        print("  1. Go to your WordPress admin panel")
        print("  2. Navigate to Tools -> Export")
        print("  3. Select 'All content'")
        print("  4. Click 'Download Export File'")
        print("  5. Save the XML file and run this script")
        sys.exit(1)

    xml_file = sys.argv[1]
    if not os.path.exists(xml_file):
        print(f"Error: File '{xml_file}' not found.")
        sys.exit(1)

    # Set up output directories
    posts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_posts')
    img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'img', 'posts')
    os.makedirs(posts_dir, exist_ok=True)
    os.makedirs(img_dir, exist_ok=True)

    # Parse and convert
    posts = parse_wordpress_export(xml_file)

    post_count = 0
    page_count = 0
    for post in posts:
        if post['type'] == 'post':
            create_jekyll_post(post, posts_dir, img_dir)
            post_count += 1
        elif post['type'] == 'page':
            # Pages go to root directory
            page_dir = os.path.dirname(os.path.abspath(__file__))
            create_jekyll_post(post, page_dir, img_dir)
            page_count += 1

    print(f"\n{'='*50}")
    print(f"Migration complete!")
    print(f"  Posts converted: {post_count}")
    print(f"  Pages converted: {page_count}")
    print(f"  Images saved to: {img_dir}")
    print(f"\nNext steps:")
    print(f"  1. Review the generated markdown files in _posts/")
    print(f"  2. Check that images downloaded correctly")
    print(f"  3. Run 'bundle exec jekyll serve' to preview")
    print(f"  4. Fix any formatting issues in individual posts")


if __name__ == '__main__':
    main()
