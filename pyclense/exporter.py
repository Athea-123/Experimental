class DataExporter:
    """Exports cleaned data"""

    def export_csv(self, df, filename="cleaned_data.csv"):
        df.to_csv(filename, index=False)
        return f"File saved as {filename}"
