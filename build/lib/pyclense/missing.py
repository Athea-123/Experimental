from .base import BaseCleaner

class MissingDataCleaner(BaseCleaner):
    def clean(self):
        """
        Executes the missing value filling process.

        This method overrides the parent `clean()` method. It performs two key operations:
        1. Fills standard pandas `NaN` values with the string "None".
        2. Identifies strings containing only whitespace (e.g., "   ") and replaces 
           them with "None".

        Returns:
            pd.DataFrame: The DataFrame with missing values filled.
        """
        self.df = self.df.fillna("None")
        self.df = self.df.replace(r'^\s*$', 'None', regex=True)
        print("[Missing] Filled missing values.")
        return self.df
