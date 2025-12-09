import sys
import os
import pandas as pd
import numpy as np
import re

# Add project root to sys.path to allow importing 'pyclense'
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from pyclense.base import BaseCleaner

class DemoCleaner(BaseCleaner):
    """
    A demonstration cleaner that processes the beach dataset. It handles:
    - Column name cleaning
    - Data type conversion for fees
    - Duplicate removal
    - Filling missing review text
    """
    def clean(self):
        """
        Applies a series of cleaning steps to the beach dataset.
        """
        if self.df is None:
            return None
        
        print("\n--- Running DemoCleaner ---")
        df = self.df

        # Step 1: Clean column names
        cleaned_cols = []
        for col in df.columns:
            c = col.strip().lower()
            c = re.sub(r'[^a-z0-9]+', '_', c)
            cleaned_cols.append(c)
        df.columns = cleaned_cols
        print(f"Cleaned column names: {list(df.columns)}")

        # Step 2: Clean and convert 'fee_usd_night' to numeric
        if 'fee_usd_night' in df.columns: # Note: The logic above will create 'fee_usd_night'
            df['fee_usd_night'] = df['fee_usd_night'].astype(str).str.replace(r'[$,+]', '', regex=True)
            df['fee_usd_night'] = pd.to_numeric(df['fee_usd_night'], errors='coerce')
            print("Cleaned and converted 'fee_usd_night' to a numeric type.")

        # Step 3: Remove duplicates
        initial_rows = len(df)
        df.drop_duplicates(inplace=True)
        print(f"Removed {initial_rows - len(df)} duplicate rows.")

        # Step 4: Handle missing 'written_review'
        if 'written_review' in df.columns:
            df['written_review'].fillna('No review written.', inplace=True)
            print("Filled missing 'written_review' values.")
        
        self.df = df
        print("--- DemoCleaner Finished ---")
        return self.df