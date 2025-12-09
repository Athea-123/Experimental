from .base import BaseCleaner

class DuplicateCleaner(BaseCleaner):
    def clean(self):
        initial = len(self)
        self._df = self._df.drop_duplicates()
        removed = initial - len(self)
        print(f"[Duplicate] Removed {removed} rows.")
        return self.df
