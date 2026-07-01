Markdown
# Intelligent Candidate Discovery & Ranking Platform

An advanced, production-grade automated screening pipeline designed to rank candidates for the founding team Senior AI Engineer position. Rather than relying on naive token counts or basic keyword matching, this system mimics an expert recruiter by applying structural 4-dimensional balancing metrics while incorporating strict anti-fraud protection guards against profile manipulation and honeypot traps.

---

## Technical Architecture Overview

The system processes candidates through a modular multi-file structure built for maximum throughput under high data velocity constraints:

1. **Memory-Isolated Streaming Utility (`load_dataset.py`)**: Implements lazy generator serialization to stream and unpack compressed `candidates.jsonl.gz` streams line-by-line. This completely avoids out-of-memory overhead bottlenecks and satisfies the hackathon's performance rules on a 16 GB baseline memory layout.
2. **Trap-Shielded Screening Engine (`scoring_engine.py`)**: Runs multi-dimensional metric calculations with early-stage qualification guards. It evaluates Skill Overlap (40%), Experience Window Balancing (30%), Growth/Shipping Velocity (15%), and Live Platform Engagement Dynamics (15%).
3. **Deterministic Execution Orchestrator (`main.py`)**: Runs the full evaluation lifecycle pipeline, handles tie-breaking edge cases cleanly by sorting on candidate ID strings as a secondary index, cuts off the final results list at exactly 100 rows, and exports a 100% spec-compliant output layout.

---

## Defensive Anti-Trap Implementations

Standard keyword indexing workflows will instantly fail because the evaluation dataset contains systematic traps. This engine implements dedicated validation checkpoints to defend against them:

* **Keyword Stuffing Checkpoint**: Detects anomalies where non-technical profiles list an excessive density of complex AI/ML proficiencies. If any core keyword list is paired with non-engineering titles (e.g., Marketing, Content Writing), the profile is downgraded or filtered out automatically.
* **Honeypot Account Isolation**: Isolates synthetic accounts that mimic a perfect technical fit on paper but present dead or impossible behavioral profiles (e.g., listing over 10 distinct expert proficiencies while maintaining a 0% profile completeness score and zero public GitHub repository check-in activity logs).
* **The IT Services Constraint**: Correctly parses current industry data fields from the nested profile layout to identify and down-weight profiles rooted heavily within consulting, outsourcing, or system-integrator segments per the target job specifications.
* **Shipper Archetype Tokenizer**: Finds true software builders by shifting emphasis away from buzzword terms toward plain-language shipping metrics (such as mention of validation pipelines, ab testing, latency optimization, NDCG/MRR metrics, and production deployment text structures).

---

## Core Operational Weight Configuration

Final composite alignment scoring is calculated using the following distributed model:

| Dimension | Primary Metric Checked | Target Focus Alignment | Model Weight |
| :--- | :--- | :--- | :--- |
| **Skill Match** | Tech Intersection Density | Core ML, Embeddings, Hybrid Search, Python | 40% |
| **Experience Fit** | Profile Years Field Tracking | Optimal target window calibration (5 to 9 Years) | 30% |
| **Growth Signals** | Career History Velocity Text | High shipping signals, title trajectory, leadership | 15% |
| **Platform Behavior** | Live Activity Analytics Logs | Open to work status, active login dates, response rates | 15% |

---

## Project Structure Layout

candidate-ranking-system/
├── src/
│   ├── main.py                  # Primary orchestrator pipeline execution entry point
│   ├── load_dataset.py          # Lazy streaming data utilities and text parsers
│   ├── scoring_engine.py        # 4D scoring algorithms and honeypot defenses
│   ├── generate_presentation.py # Automated summary slide generation engine
│   └── test_quick.py            # Local validation script
├── output/
│   ├── team_submission.csv      # Strictly formatted 4-column submission file
│   └── ranked_candidates.json   # Internal performance metadata cache payload
├── requirements.txt             # Python dependent framework environment pinned references
├── README.md                    # Complete technical documentation manual
└── GITHUB_SETUP.md              # Deployment guide


---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- System environment dependencies listed inside `requirements.txt`

### Installation

```bash
# Clone the repository workspace
git clone [https://github.com/FeroziBegam/candidate-ranking-system.git](https://github.com/FeroziBegam/candidate-ranking-system.git)
cd candidate-ranking-system

# Install all dependent modules
pip install -r requirements.txt
```
### Execution
```Bash
# Step 1: Run the main analytics pipeline (Provide path containing candidates file)
python src/main.py ./data

# Step 2: Automate PowerPoint presentation summary asset updates
python src/generate_presentation.py

```
### Submission Output Compliance
The output engine writes directly to output/team_submission.csv ensuring exact structural schema compatibility:

Exact Columns: candidate_id,rank,score,reasoning matching specified ordering definitions.

Strict Cut-Off: Outputs exactly 100 rows containing the top recommendation choices.

Deterministic Ranks: Ranks track monotonically using integers from 1 through 100 exactly once.

Monotonicity: Score fields track as strictly non-increasing down through the sequence.

### License
This project is open-source software licensed under the MIT License.
