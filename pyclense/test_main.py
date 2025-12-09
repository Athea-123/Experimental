"""
Description: A test script to demonstrate and verify the functionality of the cleaning modules.
             It loads data, runs duplicate removal, missing value filling, and standardization,
             then saves the result.
"""
import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import duplicate
import missing
import standardizer

try:
    df = pd.read_csv('data/dataset.csv')
except FileNotFoundError:
    df = pd.read_csv('../data/dataset.csv')

# 1. Remove Duplicates
df = duplicate.cull_dupes(df)

# 2. Fill Missing Values
df = missing.fill_missing(df)

# 3. Standardize Dates and Text
df = standardizer.standardize_data(df)

# Save Result
output_path = 'data/cleaned_dataset.csv'

# Ensure directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print("Processing complete!")