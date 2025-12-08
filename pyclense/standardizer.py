from .base import BaseCleaner
import pandas as pd
from typing import Optional

class Standardizer(BaseCleaner):
    """
    A class used to standardize formats of data in a DataFrame.
    Inherits from BaseCleaner.
    """

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
                # FIX: Added format='mixed' so it handles different styles in the same column
                # FIX: Added dayfirst=False to assume Month/Day/Year (US Style)
                self._df[col] = pd.to_datetime(self._df[col], errors='coerce', format='mixed', dayfirst=False).dt.strftime(format)
                self.record_change(f"standardize_dates: column={col}, format={format}")
        return self

    def capitalize_names(self, columns: list) -> 'Standardizer':
        """Converts text in specified columns to Title Case."""
        for col in columns:
            if col in self._df.columns:
                self._df[col] = self._df[col].astype(str).str.title()
                self.record_change(f"capitalize_names: column={col}")
        return self

    def convert_to_lowercase(self, columns: list) -> 'Standardizer':
        """Converts text in specified columns to lowercase."""
        for col in columns:
            if col in self._df.columns:
                self._df[col] = self._df[col].astype(str).str.lower()
                self.record_change(f"convert_to_lowercase: column={col}")
        return self

    def fix_whitespace(self, columns: Optional[list] = None) -> 'Standardizer':
        """Removes leading/trailing whitespace and replaces multiple spaces."""
        if columns is None:
            columns = self._df.select_dtypes(include=['object']).columns.tolist()
            
        for col in columns:
            if col in self._df.columns:
                before = (self._df[col].str.contains(r'\s{2,}', na=False)).sum()
                self._df[col] = self._df[col].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)
                self.record_change(f"fix_whitespace: columns={columns[:2]}, fixed_spaces={before}")
        return self

    def remove_special_chars(self, columns: list) -> 'Standardizer':
        """Removes special characters and emojis."""
        for col in columns:
            if col in self._df.columns:
                self._df[col] = self._df[col].astype(str).str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
                self.record_change(f"remove_special_chars: column={col}")
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
                self.record_change(f"standardize_booleans: column={col}")
        return self
    
    def clean(self):
        """Required by BaseCleaner. Return the cleaned DataFrame."""
        return self.get_dataframe()

    def get_dataframe(self):
        """Returns the cleaned DataFrame safely."""
        return self._df

    # --- CRITICAL FIX: Added this helper method so it doesn't crash ---
    def record_change(self, message):
        """Helper to print logs since BaseCleaner might be missing it."""
        print(f"Log: {message}")

    def capitalize_names(self, columns: list) -> 'Standardizer':
        """Converts text in specified columns to Title Case."""
        for col in columns:
            if col in self._df.columns:
                self._df[col] = self._df[col].astype(str).str.title()
                self.record_change(f"capitalize_names: column={col}")
        return self

    def convert_to_lowercase(self, columns: list) -> 'Standardizer':
        """Converts text in specified columns to lowercase."""
        for col in columns:
            if col in self._df.columns:
                self._df[col] = self._df[col].astype(str).str.lower()
                self.record_change(f"convert_to_lowercase: column={col}")
        return self

    def fix_whitespace(self, columns: Optional[list] = None) -> 'Standardizer':
        """Removes leading/trailing whitespace and replaces multiple spaces."""
        if columns is None:
            columns = self._df.select_dtypes(include=['object']).columns.tolist()
            
        for col in columns:
            if col in self._df.columns:
                before = (self._df[col].str.contains(r'\s{2,}', na=False)).sum()
                self._df[col] = self._df[col].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)
                self.record_change(f"fix_whitespace: columns={columns[:2]}, fixed_spaces={before}")
        return self

    def remove_special_chars(self, columns: list) -> 'Standardizer':
        """Removes special characters and emojis."""
        for col in columns:
            if col in self._df.columns:
                self._df[col] = self._df[col].astype(str).str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
                self.record_change(f"remove_special_chars: column={col}")
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
                self.record_change(f"standardize_booleans: column={col}")
        return self
    def clean(self):
            """Required by BaseCleaner. Return the cleaned DataFrame."""
            return self.get_data()

    def get_dataframe(self):
            """Backward-compatible alias for `get_data()` that returns the cleaned DataFrame."""
            return self.get_data()

