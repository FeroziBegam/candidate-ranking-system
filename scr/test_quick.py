"""
Quick Test Diagnostics Utility
Verifies data loading, schema extraction, and 4D evaluation on a small candidate pool sample.
Run this script to sanity-check workspace health before running the full main pipeline.
"""

import sys
from pathlib import Path

# Safely import updated system modules
from load_dataset import (
    load_candidates_jsonl,
    load_job_description,
    extract_candidate_features,
    extract_job_features,
)
from scoring_engine import AdvancedScoringEngine

def quick_test(data_path: str) -> bool:
    """Runs end-to-end scoring check on a localized 10-record pool slice."""
    
    print("\n" + "="*70)
    print("QUICK TEST DIAGNOSTICS - Sample Pool Execution Run")
    print("="*70)
    
    # Step 1: Load testing subset slice
    print("\n[1] Loading 10 sample candidates from stream space...")
    candidates = load_candidates_jsonl(data_path, max_records=10)
    
    if not candidates:
        print("Error: Failed to load candidates from target path location.")
        return False
        
    # Step 2: Extract job specifications
    print("\n[2] Loading job description metadata attributes...")
    job_text = load_job_description(data_path)
    job_features = extract_job_features(job_text)
    
    print(f"    Target Skills Monitored: {job_features['required_skills'][:6]}")
    print(f"    Target Seniority Window: {job_features['required_years']} years")
    
    # Step 3: Instantiate advanced evaluation module
    print("\n[3] Synchronizing advanced multi-dimensional scoring engine...")
    engine = AdvancedScoringEngine()
    results = []
    
    print("\n[4] Running test records evaluation loop...")
    for idx, raw_candidate in enumerate(candidates, 1):
        if not raw_candidate or 'candidate_id' not in raw_candidate:
            continue
            
        # Run features conversion and evaluation metrics sequentially
        feat = extract_candidate_features(raw_candidate)
        score, reasoning = engine.evaluate_candidate(raw_candidate)
        
        results.append({
            'id': feat['id'],
            'name': feat['name'],
            'score': score,
            'years': feat['years_experience'],
            'industry': feat['current_industry'],
            'reasoning': reasoning
        })
        print(f"    Profile {idx}/10: ID={feat['id']} Name={feat['name']} -> Mapped Score: {score}")

    # Step 4: Sort recommendations descending to simulate ranking lifecycle
    results.sort(key=lambda x: (-x['score'], x['id']))
    
    # Step 5: Render performance table display layout
    print("\n" + "="*70)
    print("LOCAL SHORTLIST SAMPLE SIMULATION VIEW")
    print("="*70)
    print(f"{'Rank':<5} {'Candidate ID':<13} {'Name':<20} {'Score':<8} {'Experience':<10}")
    print("-" * 65)
    
    for rank_idx, res in enumerate(results, 1):
        name_trunc = res['name'][:18]
        print(f"{rank_idx:<5} {res['id']:<13} {name_trunc:<20} {res['score']:<8.4f} {res['years']:<10.1f}")
        
    print("\nSample Specific Breakdown Point Reasoning:")
    for res in results[:2]:
        print(f"  - ID {res['id']}: {res['reasoning']}")
        
    print("\n" + "="*70)
    print("Quick test diagnostics completed successfully.")
    print("="*70)
    print("\nNext structural execution phase: Run 'python src/main.py' for full ranking.")
    return True

if __name__ == "__main__":
    # Handle user path arguments seamlessly
    if len(sys.argv) > 1:
        input_dir = sys.argv[1]
    else:
        input_dir = input("Enter path to extracted dataset directory: ").strip()
        
    resolver = Path(input_dir)
    if not resolver.exists():
        print(f"Target directory location path not found: {resolver}")
        sys.exit(1)
        
    success = quick_test(str(resolver))
    sys.exit(0 if success else 1)