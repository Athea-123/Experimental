import pandas as pd
from abc import ABC, abstractmethod

class BaseCleaner(ABC):
    """Base class for all cleaners"""

    def __init__(self, df: pd.DataFrame):
        self._df = df.copy()  # encapsulation
        self._log = []

    def get_data(self):
        return self._df

    def record_change(self, message: str):
        self._log.append(message)

    def get_log(self):
        return self._log

    @abstractmethod
    def clean(self):
        pass
