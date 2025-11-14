# ⚡ Quick Start Checklist - Publish to GitHub in 10 Minutes

## Before You Start
- [ ] GitHub account (create at github.com if needed)
- [ ] Git installed on your computer
- [ ] All files downloaded from the github folder

---

## Step 1: Customize Files (2 minutes)

### Edit README.md
Find and replace ALL instances of:
- `jiangweiatgithub` → your actual GitHub username
- `Your Name` → your actual name  
- `polytrans@gmail.com` → your actual email

**Quick find/replace:**
- Windows: Ctrl+H
- Mac: Cmd+F then replace
- VS Code/Notepad++: Use Find & Replace

### Edit LICENSE
Replace:
- `Wei Jiang` → your actual name

---

## Step 2: Set Up Git (2 minutes)

Open Terminal/Command Prompt:

```bash
# Configure Git (only needed once)
git config --global user.name "Your Name"
git config --global user.email "polytrans@gmail.com"

# Navigate to your project folder
cd path/to/samaltmem

# Initialize repository
git init
git add .
git commit -m "Initial commit: SamAltmem v4.0"
```

---

## Step 3: Create GitHub Repository (2 minutes)

1. Go to: https://github.com/new
2. Repository name: `samaltmem`
3. Description: "Python tool to extract alt-trans from XLIFF and convert to TMX"
4. Choose: **Public**
5. **DON'T** check any boxes (no README, no .gitignore)
6. Click: **Create repository**
7. **Keep this page open!**

---

## Step 4: Connect & Push (2 minutes)

Copy these commands from the GitHub page (they'll have your username):

```bash
# Connect to GitHub
git remote add origin https://github.com/YOUR_USERNAME/samaltmem.git
git branch -M main
git push -u origin main
```

When asked for password, use **Personal Access Token**:
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Select: `repo` scope
4. Copy token
5. Use token as password

---

## Step 5: Enhance Repository (2 minutes)

On your repository page:

1. **Add description:**
   - Click ⚙️ next to "About"
   - Description: "Python tool to extract alt-trans from XLIFF and convert to TMX"
   - Add topics: `xliff`, `tmx`, `translation`, `localization`, `python`
   - Save

2. **Create first release:**
   - Click "Releases" → "Create a new release"
   - Tag: `v4.0.0`
   - Title: `v4.0.0 - Initial Release`
   - Description: Copy from CHANGELOG.md
   - Publish

---

## ✅ Done!

Your repository is live at:
```
https://github.com/YOUR_USERNAME/samaltmem
```

---

## What to Do Next

### Share It!
- [ ] Share on LinkedIn
- [ ] Post on translation forums
- [ ] Tell colleagues
- [ ] Submit to awesome lists

### Maintain It
- [ ] Watch for issues
- [ ] Respond to questions
- [ ] Accept pull requests
- [ ] Create new releases

### Promote It
- [ ] Star your own repository ⭐
- [ ] Ask friends to star it
- [ ] Write a blog post
- [ ] Create a demo video

---

## Common Issues

### Git not found
**Fix:** Install Git from git-scm.com

### Permission denied
**Fix:** Use Personal Access Token instead of password

### Repository exists
**Fix:** Choose different name or delete existing repository

### Push rejected
**Fix:** 
```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

---

## Commands Reference

### Update repository later:
```bash
# Make changes to files
git add .
git commit -m "Description of changes"
git push
```

### Create new release:
```bash
git tag -a v4.1.0 -m "Version 4.1.0"
git push origin v4.1.0
# Then create release on GitHub website
```

---

## Need Help?

📖 **Full guide:** Read `GITHUB_PUBLISHING_GUIDE.md`  
🔍 **GitHub docs:** https://docs.github.com  
❓ **Ask:** Open an issue in your repository  

---

**Total time: ~10 minutes** ⏱️

**Difficulty: Easy** 😊

**Result: Professional open-source project** 🎉
