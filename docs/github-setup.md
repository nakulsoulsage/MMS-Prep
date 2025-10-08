# 🚀 GitHub Setup Guide

**How to push your MMS-Prep repository to GitHub**

---

## Prerequisites

- GitHub account (create at github.com if you don't have one)
- Git installed on your system (already done ✅)
- Repository initialized locally (already done ✅)

---

## Step-by-Step Guide

### Step 1: Create GitHub Repository

1. Go to https://github.com
2. Log in to your account
3. Click the "+" icon in top right → "New repository"
4. Fill in details:
   - **Repository name:** `MMS-Prep`
   - **Description:** "Comprehensive study guide generator for MMS/MBA students - Zero training required"
   - **Visibility:**
     - ✅ Public (if you want to share with others)
     - ✅ Private (if you want to keep it personal)
   - **DO NOT** initialize with README (we already have one)
5. Click "Create repository"

### Step 2: Connect Local Repo to GitHub

GitHub will show you commands. Use these in your terminal:

```bash
cd "/mnt/e/AI and Projects/MMS-Prep"

# Add remote origin (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/MMS-Prep.git

# Verify remote is added
git remote -v
```

**Example:**
```bash
git remote add origin https://github.com/nakulnandanwar/MMS-Prep.git
```

### Step 3: Make Initial Commit

```bash
# Stage all files
git add .

# Create initial commit
git commit -m "Initial commit: MMS-Prep study guide generator

- Added comprehensive README
- Created reusable template system
- Included Finance guide example
- Added configuration system
- Created Claude Code prompt template
- Added documentation (how-to-use, customization guides)
- Set up directory structure
- Included .gitignore"

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 4: Verify on GitHub

1. Go to https://github.com/YOUR_USERNAME/MMS-Prep
2. You should see all your files
3. README.md will be displayed automatically

---

## Making Future Updates

After making changes to files:

```bash
cd "/mnt/e/AI and Projects/MMS-Prep"

# Stage changes
git add .

# Commit with descriptive message
git commit -m "Add: Description of what you added/changed"

# Push to GitHub
git push
```

**Examples of good commit messages:**
```bash
git commit -m "Add: Marketing Analytics configuration example"
git commit -m "Update: Improved Claude Code prompt template"
git commit -m "Add: New generated guide for Operations Management"
git commit -m "Fix: Corrected styling in template"
git commit -m "Docs: Updated how-to-use guide with troubleshooting"
```

---

## Working with Different Topics

When you generate a new study guide:

```bash
# After generating a guide (e.g., Marketing_Guide.html)
git add generated/Marketing_Guide.html
git add configs/marketing-config.json  # if you created new config
git commit -m "Add: Marketing Analytics study guide"
git push
```

---

## Branching (Optional - Advanced)

If you want to experiment without affecting main version:

```bash
# Create new branch for experimentation
git checkout -b experiment/new-template

# Make changes...

# Commit changes
git add .
git commit -m "Experiment: Testing new template design"

# Push branch
git push -u origin experiment/new-template

# If you like it, merge back to main
git checkout main
git merge experiment/new-template
git push
```

---

## Useful Git Commands

```bash
# Check status (what's changed)
git status

# See commit history
git log --oneline

# See what changed in files
git diff

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard all local changes (careful!)
git reset --hard HEAD

# Pull latest from GitHub
git pull

# Clone on another computer
git clone https://github.com/YOUR_USERNAME/MMS-Prep.git
```

---

## Repository Structure on GitHub

After pushing, your GitHub repo will look like:

```
MMS-Prep/
├── README.md                    (Displays on GitHub homepage)
├── .gitignore
├── templates/
├── configs/
│   ├── finance-example.json
│   └── template-config.json
├── generated/
│   └── Finance_Mastery_Manual.html (example)
├── scripts/
│   └── claude-code-prompt.md
├── docs/
│   ├── how-to-use.md
│   ├── github-setup.md
│   └── configuration-guide.md
└── resources/
```

---

## Sharing Your Repository

### Make it Public

To share with classmates:

1. Go to repository on GitHub
2. Settings → Danger Zone → "Change visibility"
3. Choose "Public"

### Share Link

Share: `https://github.com/YOUR_USERNAME/MMS-Prep`

Others can:
- View your code
- Clone the repository
- Create their own study guides using your system
- Fork and customize

### Collaboration

If you want others to contribute:

1. Settings → Collaborators
2. Add their GitHub username
3. They can now push changes

---

## Best Practices

1. **Commit Often:** Don't wait to make huge commits
2. **Descriptive Messages:** Explain what and why
3. **Pull Before Push:** If collaborating, always pull first
4. **Don't Commit Sensitive Info:** Use .gitignore for private configs
5. **Tag Releases:** Tag stable versions
   ```bash
   git tag -a v1.0 -m "First stable version"
   git push --tags
   ```

---

## Troubleshooting

### "Permission denied" when pushing

Use personal access token instead of password:

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token with "repo" scope
3. Use token as password when pushing

Or set up SSH keys (more permanent solution):
https://docs.github.com/en/authentication/connecting-to-github-with-ssh

### "Rejected - non-fast-forward"

Someone else pushed changes:

```bash
git pull --rebase
git push
```

### Accidentally committed large file

```bash
# Remove from Git but keep locally
git rm --cached path/to/large/file
echo "path/to/large/file" >> .gitignore
git commit -m "Remove large file from Git"
git push
```

---

## Using MMS-Prep Across Multiple Computers

### On your new computer:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/MMS-Prep.git

# Navigate into it
cd MMS-Prep

# You're ready to use it!
```

### Keep both computers in sync:

**Computer 1:**
```bash
git add .
git commit -m "Added new guide"
git push
```

**Computer 2:**
```bash
git pull  # Downloads changes from Computer 1
```

---

## GitHub Features to Use

### 1. Releases

Create releases for major versions:
- Go to repository → Releases → Create new release
- Tag version (v1.0, v1.1, etc.)
- Describe what's new

### 2. Issues

Track improvements or bugs:
- Go to Issues tab
- Create issue: "Add template for Data Science topics"

### 3. README Badges

Add status badges to README:
```markdown
![Last Commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/MMS-Prep)
![Repo Size](https://img.shields.io/github/repo-size/YOUR_USERNAME/MMS-Prep)
```

### 4. GitHub Pages (Optional)

Host your study guides:
1. Settings → Pages
2. Source → main branch → /docs folder
3. Your guides will be accessible at: https://YOUR_USERNAME.github.io/MMS-Prep/

---

## Next Steps

1. [ ] Create GitHub account (if needed)
2. [ ] Create MMS-Prep repository
3. [ ] Connect local repo to GitHub
4. [ ] Make initial commit
5. [ ] Push to GitHub
6. [ ] Share link with classmates (optional)
7. [ ] Set up on other computer (optional)

**Your study guide system is now backed up and shareable! 🎉**

---

## Questions?

- GitHub Docs: https://docs.github.com
- Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf
- GitHub Learning Lab: https://lab.github.com/

**Good luck! 🚀**
