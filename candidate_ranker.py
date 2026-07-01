import json
import gzip
import pandas as pd
import numpy as np
from pathlib import Path

# STEP 1: LOAD AND EXPLORE DATA

class DataLoader:
    """Loads and explores the candidate and job data safely"""
    
    def __init__(self, data_path):
        """
        Initialize with path to extracted dataset
        
        Expected structure:
        data_path/
          ├── candidates.jsonl.gz (or candidates.jsonl)
          └── candidate_schema.json
        """
        self.data_path = Path(data_path)
        self.candidates = []
        self.schema = None
    
    def load_candidates(self, filename="candidates.jsonl.gz", max_records=1000):
        """
        Load candidate profiles line-by-line to safely handle JSONL formatting 
        and prevent memory bloat.
        """
        try:
            # Automatic fallback if file is already unzipped
            filepath = self.data_path / filename
            if not filepath.exists() and filename == "candidates.jsonl.gz":
                filepath = self.data_path / "candidates.jsonl"
                filename = "candidates.jsonl"
                
            if not filepath.exists():
                print(f"File not found: {filepath}")
                return None

            # Handle both gzipped and plain jsonl text streams
            open_func = gzip.open if filename.endswith('.gz') else open
            mode = 'rt' if filename.endswith('.gz') else 'r'
            
            self.candidates = []
            with open_func(filepath, mode, encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        self.candidates.append(json.loads(line))
                        # For exploration, we cap the reading to avoid long load wait times
                        if max_records and len(self.candidates) >= max_records:
                            break
                            
            print(f"Successfully sampled {len(self.candidates)} candidates for exploration")
            return self.candidates
        except Exception as e:
            print(f"Error loading candidates: {e}")
            return None
    
    def load_schema(self, filename="candidate_schema.json"):
        """Load the data schema (tells us what fields exist)"""
        try:
            filepath = self.data_path / filename
            with open(filepath, 'r', encoding='utf-8') as f:
                self.schema = json.load(f)
            print("Loaded schema successfully")
            return self.schema
        except Exception as e:
            print(f"Error loading schema: {e}")
            return None
    
    def explore_candidates(self, num_samples=2):
        """Show structure of candidate data"""
        if not self.candidates:
            print("No candidates loaded. Run load_candidates() first")
            return
        
        print(f"\n{'='*60}")
        print(f"CANDIDATE DATA STRUCTURE (Sample Size: {len(self.candidates)})")
        print(f"{'='*60}\n")
        
        # Show first N candidates
        for i, candidate in enumerate(self.candidates[:num_samples]):
            print(f"CANDIDATE #{i+1}:")
            for key, value in candidate.items():
                if isinstance(value, (list, dict)):
                    print(f"  {key}: {type(value).__name__} ({len(value)} items)")
                else:
                    val_preview = str(value)[:100]
                    print(f"  {key}: {val_preview}")
            print()
    
    def get_candidate_summary(self):
        """Show statistics about candidates"""
        if not self.candidates:
            print("No candidates loaded")
            return
        
        print(f"\n{'='*60}")
        print("CANDIDATE DATASET SUMMARY")
        print(f"{'='*60}\n")
        
        print(f"Explored candidates count: {len(self.candidates)}")
        
        if len(self.candidates) > 0:
            fields = self.candidates[0].keys()
            print(f"Fields in each candidate root: {', '.join(fields)}\n")
        
        common_fields = self._find_common_fields()
        if common_fields:
            print("Common fields across evaluated candidates:")
            for field in common_fields:
                print(f"  - {field}")
    
    def _find_common_fields(self):
        """Find fields that exist in all or most candidates"""
        if not self.candidates or len(self.candidates) == 0:
            return []
        
        field_counts = {}
        for candidate in self.candidates:
            for field in candidate.keys():
                field_counts[field] = field_counts.get(field, 0) + 1
        
        threshold = len(self.candidates) * 0.8
        return [f for f, count in field_counts.items() if count >= threshold]

# RUN EXPLORATION

if __name__ == "__main__":
    print("🚀 CANDIDATE RANKING SYSTEM - Data Exploration\n")
    
    data_path = input("Enter path to extracted dataset: ").strip()
    
    loader = DataLoader(data_path)
    
    print("\n[1] Loading candidate data sample...")
    loader.load_candidates(filename="candidates.jsonl.gz", max_records=100)
    
    print("\n[2] Loading schema...")
    loader.load_schema()
    
    print("\n[3] Exploring candidates...")
    loader.explore_candidates(num_samples=2)
    
    print("\n[4] Dataset summary...")
    loader.get_candidate_summary()
    
    print("\nData exploration complete!")
    print("Next step: Fix our pipeline's smart data loader.")