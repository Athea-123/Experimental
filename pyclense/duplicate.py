import pandas as pd

def cull_dupes(df):
    """
    Removes duplicate rows from the DataFrame.

    This function identifies duplicate rows based on all columns and removes them,
    keeping the first occurrence. It prints the number of duplicate rows removed
    to the console.

    Args:
        df (pd.DataFrame): The input DataFrame containing potential duplicates.

    Returns:
        pd.DataFrame: A new DataFrame with duplicate rows removed.
    """
    initial_count = len(df)
    df_clean = df.drop_duplicates()
    final_count = len(df_clean)
    print(f"Removed {initial_count - final_count} duplicate rows.")
    return df_clean