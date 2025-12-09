from .base import BaseCleaner

class DuplicateCleaner(BaseCleaner):
    def clean(self):
        """
        Executes the duplicate removal process.

        This method overrides the parent `clean()` method. It identifies duplicate
        rows across the entire DataFrame, removes them (keeping the first occurrence),
        and prints a summary of how many rows were removed.

        Returns:
            pd.DataFrame: The DataFrame with duplicates removed.
        """
        initial = len(self)
        self.df = self.df.drop_duplicates()
        removed = initial - len(self)
        print(f"[Duplicate] Removed {removed} rows.")
        return self.df
