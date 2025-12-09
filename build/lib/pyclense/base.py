import pandas as pd
import os
from abc import ABC, abstractmethod

class BaseCleaner(ABC):
    def __init__(self, data=None):
        if data is None:
            self._df = None
            self.filepath = None
        elif isinstance(data, pd.DataFrame):
            self._df = data.copy()
            self.filepath = None
        elif isinstance(data, BaseCleaner):
            self._df = data.df
            self.filepath = data.filepath
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
        if self._df is None:
            raise ValueError("No DataFrame loaded. Cannot save to CSV.")
        self._df.to_csv(output_path, index=False)
        print(f"Saved to {output_path}")
    
    @abstractmethod
    def clean(self):
        """
        Abstract method for cleaning the dataframe.
        Subclasses must implement this method to perform specific cleaning operations.

        Raises:
            NotImplementedError: If a subclass does not implement the clean() method.
        """
        raise NotImplementedError("Subclasses must implement the clean() method.")

    def __repr__(self):
        return f"<{self.__class__.__name__} | Rows: {len(self)}>"

    def __len__(self):
        return len(self._df) if self._df is not None else 0

    def __getitem__(self, index):
        if self._df is None:
            raise ValueError("No DataFrame loaded. Cannot access rows.")
        return self._df.iloc[index]