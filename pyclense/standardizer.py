import pandas as pd
from .base import BaseCleaner

class FormatStandardizer(BaseCleaner):
    def __init__(self, data=None, date_cols=None, text_cols=None):
        super().__init__(data)
        self.date_cols = date_cols if date_cols else []
        self.text_cols = text_cols
    
    def clean(self):
        if self.df is None:
            return None
        
        # Standardize date columns
        for col in self.date_cols:
            if col in self.df.columns:
                self.df[col] = pd.to_datetime(
                    self.df[col], errors='coerce', format='mixed'
                ).dt.strftime('%Y-%m-%d')
        
        # Determine which text columns to clean
        cols_to_clean = self.text_cols
        if cols_to_clean is None:
            cols_to_clean = self.df.select_dtypes(include=['object']).columns
        
        # Clean special characters from text columns
        for col in cols_to_clean:
            if col in self.df.columns and col not in self.date_cols:
                self.df[col] = self.df[col].apply(
                    lambda x: x.encode('ascii', 'ignore').decode('ascii').strip() if isinstance(x, str) else x
                )
        
        print(f"[Standardizer] Processed {len(self.date_cols)} date column(s) and relevant text columns.")
        return self.df
