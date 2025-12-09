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
        if filepath.endswith(('.xls', '.xlsx')):
            return pd.read_excel(filepath)
        return pd.read_csv(filepath, encoding='utf-8-sig')

    def save_data(self, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self._df.to_csv(output_path, index=False)
        print(f"Saved to {output_path}")

    def clean(self):
        raise NotImplementedError("Subclasses must implement the clean() method.")

    def __repr__(self):
        return f"<{self.__class__.__name__} | Rows: {len(self)}>"

    def __len__(self):
        return len(self._df) if self._df is not None else 0

    def __getitem__(self, index):
        return self._df.iloc[index]