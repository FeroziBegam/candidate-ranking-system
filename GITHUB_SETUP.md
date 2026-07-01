```markdown
# GitHub Setup & Deployment

## Quick Summary

You have 3 things to submit:
1. GitHub Repo (clean code + README)
2. PDF Presentation (your approach + results)
3. CSV Output (ranked candidates)

This guide walks you through creating and pushing everything to GitHub.

---

## Step 1: Create GitHub Repository

### Option A: Via GitHub Website (Easiest)

1. Go to: https://github.com/new
2. Fill in:
   - **Repository name:** `candidate-ranking-system`
   - **Description:** "AI-powered candidate ranking using multi-dimensional scoring"
   - **Visibility:** `Public` (so judges can see it)
   - **Initialize with README:** `No` (we already have one)
3. Click **Create repository**
4. Copy the repository URL (you'll need it next)

### Option B: Via Git Command Line

```bash
# Create new repo locally first
git init candidate-ranking-system
cd candidate-ranking-system
git remote add origin [https://github.com/YOUR_USERNAME/candidate-ranking-system.git](https://github.com/YOUR_USERNAME/candidate-ranking-system.git)

```

---

## Step 2: Organize Your Local Files

Create this folder structure:

```
candidate-ranking-system/
├── src/
│   ├── main.py
│   ├── load_dataset.py
│   ├── scoring_engine.py
│   ├── generate_presentation.py
│   ├── test_quick.py
│   └── __init__.py (empty file)
├── output/
│   ├── team_submission.csv
│   ├── ranked_candidates.json
│   └── presentation.pdf
├── docs/
│   ├── APPROACH.md
│   └── TECHNICAL_DETAILS.md
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE

```

---

## Step 3: Create .gitignore

Create a `.gitignore` file to prevent pushing large data binaries or temporary cache directories to Git:

```
# Data files (too large)
data/
*.jsonl
*.jsonl.gz
*.docx

# Python bytecode and caches
__pycache__/
*.pyc
*.pyo
*.pyd
.pytest_cache/

# IDE files
.vscode/
.idea/
*.swp

# OS generated files
.DS_Store
Thumbs.db

# Virtual environments
venv/
env/

```

---

## Step 4: Initialize Git & Push

```bash
# Navigate to your project folder
cd candidate-ranking-system

# Initialize git
git init

# Add all files
git add .

# Commit your changes
git commit -m "Initial commit: Intelligent candidate ranking system

- 4-dimensional scoring engine (skill, experience, growth, behavior)
- Multi-file streaming architecture with clear separation of concerns
- Processes massive gzipped JSONL datasets efficiently without disk unzipping
- Generates compliant 4-column ranking output CSV and presentation slide summaries"

# Add remote linking to your GitHub repo
git remote add origin [https://github.com/YOUR_USERNAME/candidate-ranking-system.git](https://github.com/YOUR_USERNAME/candidate-ranking-system.git)

# Push the code up to GitHub main branch
git branch -M main
git push -u origin main

```

---

## Step 5: Create Release Tag

Tag your final submission to timestamp your final delivery snapshot:

```bash
git tag -a v1.0 -m "Final submission snapshot for evaluation"
git push origin v1.0

```

---

## Step 6: Verify on GitHub

Check your repository at: `https://github.com/YOUR_USERNAME/candidate-ranking-system`

Verify that:

* All Python source scripts are visible
* README.md displays cleanly on the main page
* requirements.txt is complete
* Folder hierarchies match perfectly

---

## Step 7: Create Submission Folder

For seamless entry into the evaluation portal, keep your core artifacts organized:

```
submission/
├── team_submission.csv           # Strictly formatted 4-column CSV matching spec
├── PRESENTATION.pdf              # Your approach slide deck converted to PDF
└── README.md                     # Direct workspace reference linking your code repo

```

---

## Git Commit Best Practices

### Initial Commit

```bash
git commit -m "Initial commit: Core engine implementation"

```

### After Running Pipeline

```bash
git commit -m "Add: Final processing run results saved to output"

```

### After Generating Presentation

```bash
git commit -m "Add: Presentation automation slide layout updates"

```

---

## Helpful Git Reference Commands

```bash
# Check working changes state
git status

# View compact commit history
git log --oneline

# Undo your last commit safely (before running a push)
git reset --soft HEAD~1

# Push code updates upstream
git push origin main

# Pull down upstream server updates
git pull origin main

```

---

## PDF Presentation Submission

### Convert PowerPoint to PDF

**Option 1: Microsoft PowerPoint**

* Open your generated `presentation.pptx`
* File -> Export As -> PDF Document

**Option 2: LibreOffice (Headless CLI Linux)**

```bash
libreoffice --headless --convert-to pdf output/presentation.pptx

```

---

## Final Submission Checklist

* [ ] GitHub repository visibility is set to PUBLIC
* [ ] README.md explicitly documents setup steps and architectural rules
* [ ] Requirements text incorporates all dependent framework extensions
* [ ] Output CSV follows the 4-column spec format: candidate_id,rank,score,reasoning
* [ ] Output CSV contains exactly 100 rows matching your top ranked recommendations
* [ ] No large data arrays or compressed source archives have been committed to history
* [ ] Formatting prints use clean text without cross or check symbols

---

## Troubleshooting

### Error: "fatal: not a git repository"

```bash
git init

```

### Error: "permission denied" when pushing

```bash
git remote set-url origin [https://github.com/YOUR_USERNAME/candidate-ranking-system.git](https://github.com/YOUR_USERNAME/candidate-ranking-system.git)

```

### Large File Rejected by Server Hooks

```bash
git rm --cached path/to/large/file.jsonl
# Add file pattern to .gitignore and recommit

```

---

## Example README Header for GitHub

```markdown
# Intelligent Candidate Ranking System

**Problem:** Recruiters manually sort through hundreds of profiles, often missing the best candidates because keyword matching can't capture nuanced fit.

**Solution:** An AI-powered system that ranks candidates across 4 dimensions:
- Skill Match (40%)
- Experience Fit (30%)
- Growth Signals (15%)
- Platform Behavior Modifiers (15%)

## Quick Start

```bash
pip install -r requirements.txt
python main.py ./data
python generate_presentation.py

```

---

## Final Notes

**You're ready to submit when:**

1. GitHub repo has all code and README
2. PDF presentation is completed
3. CSV output is generated

**Judges will look for:**

* Clean, well-organized code
* Clear documentation
* Thoughtful approach to the problem
* Working solution that produces results
* Good README explaining your thinking

**Good luck!**

```