import pandas as pd
from pyclense import (
    MissingCleaner,
    DuplicateCleaner,
    Standardizer,
    DataExporter
)

# Load dataset from mydata folder
df = pd.read_csv("mydata/dataset.csv")

print("===== ORIGINAL DATA =====")
print(df)

# Test MissingCleaner
print("\n===== TESTING MissingCleaner =====")
missing_cleaner = MissingCleaner(df)
df_missing_cleaned = missing_cleaner.clean()
print(df_missing_cleaned)
print("Log:", missing_cleaner.get_log())

# Test DuplicateCleaner
print("\n===== TESTING DuplicateCleaner =====")
duplicate_cleaner = DuplicateCleaner(df_missing_cleaned)
df_duplicates_cleaned = duplicate_cleaner.clean()
print(df_duplicates_cleaned)
print("Log:", duplicate_cleaner.get_log())

# Test Standardizer
print("\n===== TESTING Standardizer =====")
standardizer = Standardizer(df_duplicates_cleaned)
df_standardized = standardizer.clean()
print(df_standardized)
print("Log:", standardizer.get_log())

# Test Exporter
print("\n===== TESTING DataExporter =====")
exporter = DataExporter()
message = exporter.export_csv(df_standardized, "mydata/cleaned_output.csv")
print(message)
