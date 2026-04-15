# Tales of Testing: WordPress to Jekyll Migration Guide

## Overview

Migrating **talesoftesting.com** from WordPress to Jekyll + GitHub Pages.

**What you get:** A fast, free, low-maintenance site with the Chirpy theme (same as huibschoots.nl), plus a custom Talks/Publications page with video/photo grid.

**Cost:** $0 (beyond your existing domain registration)

---

## Step 1: Export Your WordPress Content

1. Log in to your WordPress admin: `https://talesoftesting.com/wp-admin/`
2. Go to **Tools > Export**
3. Select **All content**
4. Click **Download Export File**
5. Save the `.xml` file somewhere accessible

---

## Step 2: Set Up Your Local Environment

You need Ruby and Jekyll installed. On macOS:

```bash
# Install Homebrew (if you don't have it)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Ruby
brew install ruby

# Add Ruby to your PATH (add to ~/.zshrc)
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Install Jekyll and Bundler
gem install jekyll bundler
```

---

## Step 3: Set Up the Jekyll Site

```bash
# Navigate to this project folder
cd talesoftesting-jekyll

# Install dependencies
bundle install

# Preview locally
bundle exec jekyll serve
```

Visit `http://localhost:4000` to see your site!

---

## Step 4: Migrate Your WordPress Posts

```bash
# Run the migration script with your WordPress export file
python3 migrate_wp.py path/to/your-wordpress-export.xml
```

This will:
- Convert all posts to Markdown files in `_posts/`
- Download images to `assets/img/posts/`
- Preserve categories, tags, and dates

**After migration, review a few posts** to check formatting. The HTML-to-Markdown conversion handles most cases, but complex layouts may need manual tweaks.

---

## Step 5: Add Your Avatar & Customize

1. **Avatar:** Replace `assets/img/avatar/lalit.jpg` with your profile photo
2. **About page:** Edit `_tabs/about.md` with your full bio
3. **Talks page:** Edit `_data/talks.yml` to add your real talks, videos, and publications
4. **Config:** Update `_config.yml` with your social links, GitHub username, etc.

---

## Step 6: Create GitHub Repository

```bash
# Create a new repo on GitHub (e.g., "talesoftesting.github.io" or any name)
# Then push your site:

cd talesoftesting-jekyll
git init
git add .
git commit -m "Initial Jekyll site migration from WordPress"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

---

## Step 7: Enable GitHub Pages

1. Go to your repo on GitHub
2. Navigate to **Settings > Pages**
3. Under **Build and deployment**, select **Source: GitHub Actions**
4. The included `.github/workflows/pages-deploy.yml` will handle builds automatically

Your site will be live at: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

---

## Step 8: Point Your Custom Domain

1. In your repo's **Settings > Pages**, add custom domain: `talesoftesting.com`
2. GitHub will create a `CNAME` file automatically

3. Go to your domain registrar and update DNS:

   **Option A: Apex domain (talesoftesting.com)**
   Add these A records:
   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```

   **Option B: Also add www subdomain**
   Add a CNAME record:
   ```
   www -> YOUR_USERNAME.github.io
   ```

4. Back in GitHub Pages settings, check **Enforce HTTPS**
5. Wait 15-30 minutes for DNS to propagate

---

## Step 9: Decommission WordPress

Once everything is working on the new site:
1. Keep your WordPress backup (the XML export) safe
2. Cancel your WordPress hosting plan
3. Done! You're now running for free.

---

## Day-to-Day Usage

### Writing a new blog post

Create a file in `_posts/` named `YYYY-MM-DD-your-title.md`:

```markdown
---
title: "My New Post"
date: 2024-07-15 10:00:00 +0530
categories: [Testing, Leadership]
tags: [quality, engineering]
image:
  path: /assets/img/posts/my-image.jpg
  alt: "Description of image"
---

Your content in Markdown here...
```

### Adding a new talk/video

Edit `_data/talks.yml` and add a new entry:

```yaml
- title: "My Conference Talk"
  type: video
  date: 2024-07-15
  event: "TestBash 2024"
  description: "Short description of the talk."
  video_url: "https://www.youtube.com/embed/VIDEO_ID"
  tags: [testing, leadership]
```

### Publishing

```bash
git add .
git commit -m "New post: My title"
git push
```

GitHub Actions builds and deploys automatically within ~2 minutes.

---

## File Structure Reference

```
talesoftesting-jekyll/
  _config.yml           # Site configuration
  _data/
    talks.yml           # Your talks/publications data
  _layouts/
    talks.html          # Custom media grid layout
  _posts/               # Blog posts (YYYY-MM-DD-title.md)
  _tabs/
    about.md            # About page
    archives.md         # Archives page
    categories.md       # Categories page
    tags.md             # Tags page
    talks.md            # Talks & Publications page
  assets/
    img/
      avatar/           # Your profile photo
      posts/            # Blog post images
      talks/            # Talk thumbnails
  .github/
    workflows/
      pages-deploy.yml  # Auto-deploy to GitHub Pages
  Gemfile               # Ruby dependencies
  migrate_wp.py         # WordPress migration script
```
