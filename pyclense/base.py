import pandas as pd
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)
# ---------------------------------------------------------------------

import duplicate
import missing
import standardizer

class BaseCleaner:
    """
    A class to load, clean, preview, and save datasets.

    Attributes:
        filepath (str): Path to the source data file.
        df (pd.DataFrame): The pandas DataFrame holding the data.
        change_log (list): A list of strings recording operations performed.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None
        self.change_log = []

    def load_data(self, **kwargs):
        """Loads data from CSV or Excel with UTF-8 encoding."""
        if not os.path.exists(self.filepath):
            if os.path.exists(os.path.basename(self.filepath)):
                self.filepath = os.path.basename(self.filepath)
            else:
                raise FileNotFoundError(f"File not found: {self.filepath}")

        if self.filepath.endswith(('.xls', '.xlsx')):
            self.df = pd.read_excel(self.filepath, **kwargs)
        else:
            self.df = pd.read_csv(self.filepath, encoding='utf-8-sig', **kwargs)

        msg = f"Data loaded successfully. Shape: {self.df.shape}"
        print(msg)
        self.change_log.append(msg)
        return self.df

    def run_pipeline(self):
        """Executes the cleaning pipeline."""
        if self.df is None:
            print("No data loaded. Please load data first.")
            return

        print("\n--- Running Cleaning Pipeline ---")
        
        self.df = duplicate.cull_dupes(self.df)
        self.change_log.append("Executed duplicate removal.")

        self.df = missing.fill_missing(self.df)
        self.change_log.append("Executed missing value filling.")

        self.df = standardizer.standardize_data(self.df)
        self.change_log.append("Executed standardization.")
        
        print("Pipeline Complete.")
        return self.df

    def preview_data(self, top_n=5):
        if self.df is not None:
            print(f"\n--- Data Preview (First {top_n} rows) ---")
            print(self.df.head(top_n))
            print("-----------------------------------------")

    def save_data(self, output_path):
        """Saves data to CSV or Excel with UTF-8 encoding."""
        if self.df is not None:
            directory = os.path.dirname(output_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)

            if output_path.endswith(('.xls', '.xlsx')):
                self.df.to_excel(output_path, index=False)
            else:
                self.df.to_csv(output_path, index=False, encoding='utf-8-sig')

            msg = f"Data saved to {output_path}"
            print(msg)
            self.change_log.append(msg)
        else:
            print("No data to save.")

    def set_data(self, df):
        self.df = df