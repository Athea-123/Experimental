from .base import BaseCleaner

class MissingCleaner(BaseCleaner):
    """Handles missing values"""

    def detect(self):
        return self._df[self._df.isnull().any(axis=1)]

    def fill(self, value=0):
        self._df = self._df.fillna(value)
        self.record_change(f"Filled missing values with {value}")
        return self._df

    def clean(self):
        return self.fill()
