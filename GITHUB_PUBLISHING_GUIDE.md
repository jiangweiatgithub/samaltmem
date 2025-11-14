# 🚀 Publishing to GitHub - Complete Guide

## Prerequisites

### 1. Create a GitHub Account
- Go to [https://github.com](https://github.com)
- Sign up for free
- Verify your email

### 2. Install Git
**Windows:**
- Download from [https://git-scm.com/download/win](https://git-scm.com/download/win)
- Run installer
- Use default options

**Mac:**
```bash
# Using Homebrew
brew install git

# Or use Xcode Command Line Tools
xcode-select --install
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get install git

# Fedora
sudo dnf install git
```

### 3. Configure Git
```bash
# Set your name
git config --global user.name "Your Name"

# Set your email (use GitHub email)
git config --global user.email "your.email@example.com"

# Verify
git config --list
```

---

## Step-by-Step Guide

### Step 1: Create GitHub Repository

#### Option A: Via GitHub Website (Recommended)
1. Go to [https://github.com/new](https://github.com/new)
2. Fill in repository details:
   - **Repository name**: `samaltmem`
   - **Description**: "Python tool to extract alt-trans from XLIFF files and convert to TMX format"
   - **Public** or **Private**: Choose Public
   - **DO NOT** initialize with README (we have our own)
   - **DO NOT** add .gitignore (we have our own)
   - **License**: Choose MIT License
3. Click "Create repository"
4. **Keep this page open** - you'll need the URL

#### Option B: Via GitHub CLI (Advanced)
```bash
# Install GitHub CLI first
# Then:
gh repo create samaltmem --public --description "Python tool to extract alt-trans from XLIFF files and convert to TMX format"
```

---

### Step 2: Prepare Your Local Files

Create a project folder and organize files:

```bash
# Create project directory
mkdir samaltmem
cd samaltmem

# Copy the main files (adjust paths as needed)
cp path/to/xliff_to_tmx_hybrid.py .
cp path/to/xliff_alttrans_to_tmx_parameterized.xsl .
```

Copy these repository files to your project directory:
- `README.md`
- `LICENSE`
- `requirements.txt`
- `.gitignore`
- `CHANGELOG.md`
- `CONTRIBUTING.md`

Your directory should look like:
```
samaltmem/
├── xliff_to_tmx_hybrid.py
├── xliff_alttrans_to_tmx_parameterized.xsl
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── CHANGELOG.md
└── CONTRIBUTING.md
```

---

### Step 3: Initialize Git Repository

```bash
# Navigate to your project directory
cd samaltmem

# Initialize Git repository
git init

# Check status
git status
# Should show all your files as "Untracked"
```

---

### Step 4: Stage Files

```bash
# Add all files
git add .

# Or add files individually
git add xliff_to_tmx_hybrid.py
git add xliff_alttrans_to_tmx_parameterized.xsl
git add README.md
git add LICENSE
git add requirements.txt
git add .gitignore
git add CHANGELOG.md
git add CONTRIBUTING.md

# Verify staged files
git status
# Should show files as "Changes to be committed"
```

---

### Step 5: Make Initial Commit

```bash
# Commit with message
git commit -m "Initial commit: SamAltmem v4.0"

# Verify commit
git log
```

---

### Step 6: Connect to GitHub

```bash
# Add GitHub repository as remote
# Replace YOUR_USERNAME with your actual GitHub username
git remote add origin https://github.com/YOUR_USERNAME/samaltmem.git

# Verify remote
git remote -v
```

---

### Step 7: Push to GitHub

```bash
# Push to GitHub (first time)
git push -u origin main

# If you get an error about "master" vs "main":
git branch -M main
git push -u origin main
```

#### If Asked for Credentials:

**Option 1: Personal Access Token (Recommended)**
1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a name: "SamAltmem"
4. Select scopes: `repo` (full control of private repositories)
5. Click "Generate token"
6. **Copy the token** (you won't see it again!)
7. Use token as password when pushing

**Option 2: GitHub CLI**
```bash
# Authenticate
gh auth login

# Then push
git push -u origin main
```

---

### Step 8: Verify on GitHub

1. Go to `https://github.com/YOUR_USERNAME/samaltmem`
2. You should see all your files
3. README.md will display automatically on the main page

---

## Customizing Your Repository

### Update README.md

Edit these placeholders:
```markdown
# In README.md, replace:
- `yourusername` → your actual GitHub username
- `Your Name` → your actual name
- `your.email@example.com` → your actual email
```

### Update LICENSE

```markdown
# In LICENSE, replace:
- `[Your Name]` → your actual name
```

### Create a Nice Repository Description

1. Go to your repository on GitHub
2. Click the ⚙️ (settings) gear next to "About"
3. Add:
   - **Description**: "Python tool to extract alt-trans from XLIFF and convert to TMX"
   - **Website**: Your website (optional)
   - **Topics**: Add tags like:
     - `xliff`
     - `tmx`
     - `translation`
     - `localization`
     - `cat-tools`
     - `python`
     - `translator-tools`

---

## Making Future Updates

### Step 1: Make Changes
```bash
# Edit files
nano xliff_to_tmx_hybrid.py  # or use your editor
```

### Step 2: Check Changes
```bash
git status
git diff  # See what changed
```

### Step 3: Stage Changes
```bash
git add xliff_to_tmx_hybrid.py  # specific file
# or
git add .  # all changes
```

### Step 4: Commit Changes
```bash
git commit -m "Fix UTF-16 encoding detection"
# Use descriptive commit messages
```

### Step 5: Push to GitHub
```bash
git push
```

---

## Creating Releases

### Step 1: Create a Tag
```bash
# Create annotated tag
git tag -a v4.0.0 -m "Version 4.0.0 - Hybrid mode release"

# Push tag to GitHub
git push origin v4.0.0
```

### Step 2: Create Release on GitHub
1. Go to your repository on GitHub
2. Click "Releases" (right sidebar)
3. Click "Create a new release"
4. Fill in:
   - **Tag**: Select `v4.0.0`
   - **Release title**: `v4.0.0 - Hybrid Mode`
   - **Description**: Copy from CHANGELOG.md
   - **Attach files**: Upload compiled .exe if you have one
5. Click "Publish release"

---

## Best Practices

### Commit Messages
```bash
# Good commit messages:
git commit -m "Add support for UTF-32 encoding"
git commit -m "Fix merge mode output filename generation"
git commit -m "Update README with new examples"

# Bad commit messages:
git commit -m "fix"
git commit -m "update"
git commit -m "changes"
```

### Commit Frequency
- Commit after each logical change
- Don't commit half-done work
- Commit before making big changes

### Branch Strategy
```bash
# For new features, create a branch
git checkout -b feature/add-gui

# Make changes and commit
git add .
git commit -m "Add GUI wrapper"

# Push branch
git push -u origin feature/add-gui

# Create Pull Request on GitHub
# After merge, switch back
git checkout main
git pull
```

---

## Troubleshooting

### Problem: Git not recognized
**Solution:**
```bash
# Verify Git installation
git --version

# If not found, reinstall Git
```

### Problem: Authentication failed
**Solution:**
```bash
# Use Personal Access Token instead of password
# Or use GitHub CLI:
gh auth login
```

### Problem: Push rejected
**Solution:**
```bash
# Pull latest changes first
git pull origin main

# Resolve conflicts if any
# Then push
git push
```

### Problem: Wrong files committed
**Solution:**
```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Or unstage specific file
git reset HEAD filename
```

---

## Adding Badges to README

Add at the top of README.md:

```markdown
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![GitHub release](https://img.shields.io/github/release/YOUR_USERNAME/samaltmem.svg)](https://github.com/YOUR_USERNAME/samaltmem/releases/)
[![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/samaltmem.svg)](https://github.com/YOUR_USERNAME/samaltmem/issues)
[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/samaltmem.svg)](https://github.com/YOUR_USERNAME/samaltmem/stargazers)
```

---

## Optional Enhancements

### Add GitHub Actions (CI/CD)
Create `.github/workflows/test.yml`:
```yaml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Test script
        run: python xliff_to_tmx_hybrid.py --help
```

### Add Documentation Site
Use GitHub Pages to host documentation.

### Add Issue Templates
Create `.github/ISSUE_TEMPLATE/bug_report.md`

---

## Quick Reference

### Essential Git Commands
```bash
git init                    # Initialize repository
git add .                   # Stage all changes
git commit -m "message"     # Commit changes
git push                    # Push to GitHub
git pull                    # Pull from GitHub
git status                  # Check status
git log                     # View history
git diff                    # See changes
```

### Repository URL
```
https://github.com/YOUR_USERNAME/samaltmem
```

---

## Checklist

Before publishing:
- [ ] All files in directory
- [ ] README.md updated with your info
- [ ] LICENSE has your name
- [ ] .gitignore prevents unnecessary files
- [ ] requirements.txt is correct
- [ ] Tested the script works
- [ ] Git repository initialized
- [ ] Files committed
- [ ] GitHub repository created
- [ ] Connected to remote
- [ ] Pushed to GitHub
- [ ] Verified on GitHub website

After publishing:
- [ ] Add repository description
- [ ] Add topics/tags
- [ ] Create first release
- [ ] Share with community
- [ ] Star your own repository! ⭐

---

## 🎉 Congratulations!

Your SamAltmem is now on GitHub!

**Next steps:**
1. Share the link with colleagues
2. Submit to awesome lists
3. Announce on translation forums
4. Collect feedback
5. Keep improving!

**Repository URL:**
```
https://github.com/YOUR_USERNAME/samaltmem
```

---

## Getting Help

- **GitHub Docs**: [https://docs.github.com](https://docs.github.com)
- **Git Docs**: [https://git-scm.com/doc](https://git-scm.com/doc)
- **GitHub Community**: [https://github.community](https://github.community)

---

**Need help? Open an issue in your repository or ask in the GitHub Community!**
