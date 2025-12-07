from .base import BaseCleaner

class Standardizer(BaseCleaner):
    """Standardizes text data"""

    def clean(self):
        self._df.columns = [col.strip().lower() for col in self._df.columns]
        self.record_change("Standardized column names")
        return self._df
