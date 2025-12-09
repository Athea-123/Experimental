import pandas as pd
from .base import BaseCleaner

class FormatStandardizer(BaseCleaner):
    """
    A class to fix date formats and remove special characters from text.

    It ensures all dates look the same and strips out emojis or symbols 
    that might cause issues in the dataset.
    """
    def clean(self):
        """
        Runs the formatting logic.

        It changes the 'Review Date' to a specific format (MM/DD/YYYY) and 
        removes special characters/emojis from other text fields.

        Returns:
            The dataframe with fixed dates and cleaned text.
        """
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
