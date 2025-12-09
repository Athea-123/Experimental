from .base import BaseCleaner

class MissingDataCleaner(BaseCleaner):
    def clean(self):
        self.df = self.df.fillna("None")
        self.df = self.df.replace(r'^\s*$', 'None', regex=True)
        print("[Missing] Filled missing values.")
        return self.df
