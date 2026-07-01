Markdown
# Complete Setup & Execution Guide

## Setup Timeline

You have 24 hours. Let's execute this step-by-step to guarantee a valid submission.

---

## Phase 1: Environment Setup

### 1.1 Verify Your Dataset Folder
The target directory containing your hackathon bundle files must include the following assets:
- `candidates.jsonl.gz` (The gzipped line-by-line candidate archive)
- `candidate_schema.json` (The nested database schema blueprints)
- `job_description.docx` (The founding Series A job criteria)

### 1.2 Install Python Requirements
Open your terminal in the root project folder and run:
```bash
pip install -r requirements.txt
1.3 Verify Code Architecture Location
Ensure your project files are laid out as follows inside your repository:

candidate-ranking-system/
├── src/
│   ├── main.py                  
│   ├── load_dataset.py          
│   ├── scoring_engine.py        
│   ├── generate_presentation.py 
│   └── test_quick.py            
├── requirements.txt
├── README.md
├── GITHUB_SETUP.md
└── START_HERE.md

Phase 2: Diagnostic Diagnostics
2.1 Run Quick Test Run
Execute the quick test to verify schema mapping accuracy against a small local pool subset:

Bash
python src/test_quick.py ./data
2.2 Validate Output Log Messages
Confirm the console output displays data streaming logs, calculates non-zero metrics, and outputs mock reason statements without rendering exceptions.

Phase 3: Run Full Evaluation Pipeline
3.1 Run Main Pipeline Orchestration
To process the entire candidate base securely through lazy iteration stream spaces, run:

Bash
python src/main.py ./data
3.2 Expected Console Tracking
The system handles file streaming metrics asynchronously and prints progress counters for every 10,000 processed candidate entries, completing entirely within the required 5-minute execution limit.

Phase 4: Output File Layout Validation
4.1 Check Generated Files
Bash
ls -lah output/
Verify that the execution successfully generates:

team_submission.csv (The strictly formatted top 100 final file)

ranked_candidates.json (The metadata cache block tracking weights)

4.2 Preview Top Rows Compliance
Bash
head -n 5 output/team_submission.csv
The result matrix header and columns must strictly match this order:

candidate_id,rank,score,reasoning
CAND_XXXXXXX,1,0.9234,Senior Engineer showing true product engineering background...
Phase 5: Generate Summary Slides
5.1 Create PowerPoint Deck
Run the PowerPoint automation compiler:

Bash
python src/generate_presentation.py
5.2 Export Deck to Submission PDF
Open output/presentation.pptx using Microsoft PowerPoint or Google Slides, choose "Export as PDF Document", and save the final layout directly as submission/PRESENTATION.pdf.

Phase 6: Push to Code Repositories
6.1 Initialize and Commit Source Files
Bash
git init
git add src/ requirements.txt README.md GITHUB_SETUP.md START_HERE.md
git commit -m "Complete submission: Intelligent candidate Discovery Platform"
6.2 Push to Public GitHub
Bash
git remote add origin [https://github.com/YOUR_USERNAME/candidate-ranking-system.git](https://github.com/YOUR_USERNAME/candidate-ranking-system.git)
git branch -M main
git push -u origin main
Verify via your web browser that the codebase status is set to Public so evaluate scripts can crawl it.

Final Delivery Checklist
Code Repository visibility is explicitly confirmed as PUBLIC.

The output CSV is renamed to track your assigned Team ID.

The output CSV holds exactly 100 candidates (excluding the header row).

Columns perfectly match: candidate_id, rank, score, reasoning.

Score distributions are strictly non-increasing down through the ranks.

The PDF presentation layout covers your 4D weights configuration details.

Console text interfaces omit unreadable characters or graphic symbols.