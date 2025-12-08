from .base import BaseCleaner
import pandas as pd
from typing import Optional

class Standardizer(BaseCleaner):
    """
    A class used to standardize formats of data in a DataFrame.
    Inherits from BaseCleaner.
    """

    def standardize_dates(self, columns: list, format: str = '%m/%d/%Y') -> 'Standardizer':
        """Converts specified columns to a standard date format."""
        for col in columns:
            if col in self._df.columns:
                self._df[col] = pd.to_datetime(self._df[col], errors='coerce').dt.strftime(format)
                self._log_change('standardize_dates', {'column': col, 'format': format})
        return self

    def capitalize_names(self, columns: list) -> 'Standardizer':
        """Converts text in specified columns to Title Case."""
        for col in columns:
            if col in self._df.columns:
                self._df[col] = self._df[col].astype(str).str.title()
                self._log_change('capitalize_names', {'column': col})
        return self

    def convert_to_lowercase(self, columns: list) -> 'Standardizer':
        """Converts text in specified columns to lowercase."""
        for col in columns:
            if col in self._df.columns:
                self._df[col] = self._df[col].astype(str).str.lower()
                self._log_change('convert_to_lowercase', {'column': col})
        return self

    def fix_whitespace(self, columns: Optional[list] = None) -> 'Standardizer':
        """Removes leading/trailing whitespace and replaces multiple spaces."""
        if columns is None:
            columns = self._df.select_dtypes(include=['object']).columns.tolist()
            
        for col in columns:
            if col in self._df.columns:
                before = (self._df[col].str.contains(r'\s{2,}', na=False)).sum()
                self._df[col] = self._df[col].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)
                self._log_change('fix_whitespace', {'columns': columns[:2], 'fixed_spaces': before})
        return self

    def remove_special_chars(self, columns: list) -> 'Standardizer':
        """Removes special characters and emojis."""
        for col in columns:
            if col in self._df.columns:
                self._df[col] = self._df[col].astype(str).str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
                self._log_change('remove_special_chars', {'column': col})
        return self

    def standardize_booleans(self, columns: list) -> 'Standardizer':
        """Converts Yes/No formats into standard True/False."""
        bool_map = {
            'yes': True, 'y': True, 'true': True, '1': True, 't': True,
            'no': False, 'n': False, 'false': False, '0': False, 'f': False
        }

        for col in columns:
            if col in self._df.columns:
                self._df[col] = self._df[col].astype(str).str.lower().map(bool_map)
                self._log_change('standardize_booleans', {'column': col})
        return self
    
    def clean(self):
        """Required by BaseCleaner."""
        return self

    def _log_change(self, method, details):
        """
        Helper method to log changes.
        This must be indented INSIDE the class (same level as def clean).
        """
        print(f"Log: {method} - {details}")