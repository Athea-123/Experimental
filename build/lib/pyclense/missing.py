from .base import BaseCleaner

class MissingDataCleaner(BaseCleaner):
    """
    A cleaner to handle missing data by dropping rows based on a subset of columns.
    """
    def __init__(self, data=None, subset=None):
        super().__init__(data)
        self.subset = subset

    def clean(self):
        if self.df is None:
            return None
        
        if not self.subset:
            print("[MissingDataCleaner] No subset provided; no rows were dropped.")
            return self.df
        
        initial_rows = len(self.df)
        self.df.dropna(subset=self.subset, inplace=True)
        print(f'[MissingDataCleaner] Dropped {initial_rows - len(self.df)} rows with missing values in {self.subset}.')
        return self.df
