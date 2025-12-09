import pandas as pd
import os

class BaseCleaner:
    """
    Parent class defining the blueprint for all cleaners.
    """
    
    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self._df = data.copy()
            self.filepath = None
        else:
            self.filepath = data
            self._df = self._load_data(data)

    @property
    def df(self):
        return self._df

    @df.setter
    def df(self, new_df):
        self._df = new_df

    def _load_data(self, filepath):
        """
        Protected helper method to load data from a file.

        Automatically detects CSV or Excel formats based on file extension.

        Args:
            filepath (str): The path to the file.

        Returns:
            pd.DataFrame: The loaded dataset.
        """
        if filepath.endswith(('.xls', '.xlsx')):
            return pd.read_excel(filepath)
        return pd.read_csv(filepath, encoding='utf-8-sig')

    def save_data(self, output_path):
        """
        Saves the current state of the dataframe to a CSV file.

        This method automatically creates the target directory if it does not exist.

        Args:
            output_path (str): The destination path for the CSV file.
        """
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self._df.to_csv(output_path, index=False)
        print(f"Saved to {output_path}")

    def clean(self):
        """
        Abstract method intended to be overridden by subclasses.

        This enforces Polymorphism, ensuring every child class implements its own
        specific cleaning logic.

        Raises:
            NotImplementedError: If called directly on the BaseCleaner.
        """
        raise NotImplementedError("Subclasses must implement the clean() method.")

    def __repr__(self):
        return f"<{self.__class__.__name__} | Rows: {len(self)}>"

    def __len__(self):
        return len(self._df) if self._df is not None else 0

    def __getitem__(self, index):
        return self._df.iloc[index]
