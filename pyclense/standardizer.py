import pandas as pd
from .base import BaseCleaner

class FormatStandardizer(BaseCleaner):
    def clean(self):
        if 'Review Date' in self.df.columns:
            self.df['Review Date'] = pd.to_datetime(
                self.df['Review Date'], 
                errors='coerce', 
                format='mixed', 
                dayfirst=False
            ).dt.strftime('%m/%d/%Y')
        
        for col in self.df.select_dtypes(include=['object']).columns:
            if col != 'Review Date':
                self.df[col] = self.df[col].apply(
                    lambda x: x.encode('ascii', 'ignore').decode('ascii').strip() if isinstance(x, str) else x
                )
        
        print("[Standardizer] Formatted dates and text.")
        return self.df