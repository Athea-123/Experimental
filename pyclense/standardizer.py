import pandas as pd
import warnings

def clean_text(text):
    """
    Removes special characters (emojis, non-ASCII symbols) from a string.
    Example: 'Perfect! 💙' -> 'Perfect!'
    """
    if not isinstance(text, str):
        return text
    return text.encode('ascii', 'ignore').decode('ascii').strip()

def format_date(date_str):
    """
    Converts date strings to MM/DD/YYYY format.
    This function handles mixed date formats (e.g., '10/15/2025' vs '20-Nov-2025') without warnings.
    """
    if pd.isna(date_str) or str(date_str).strip() == "" or str(date_str).lower() == "none":
        return date_str
        
    try:
        dt = pd.to_datetime(date_str, format='mixed', dayfirst=False)
        return dt.strftime('%m/%d/%Y')
    except (ValueError, TypeError, AttributeError):

        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                dt = pd.to_datetime(date_str, dayfirst=False, errors='coerce')
            
            if pd.isna(dt):
                return date_str
            return dt.strftime('%m/%d/%Y')
        except:
            return date_str

def standardize_data(df):
    """
    Applies text cleaning and date formatting to the DataFrame.

    Specifically:
    1. Formats the 'Review Date' column to 'MM/DD/YYYY' if it exists.
    2. Removes special characters from all other object (string) columns.

    Args:
        df (pd.DataFrame): The input DataFrame to standardize.

    Returns:
        pd.DataFrame: The standardized DataFrame.
    """
    # Standardize 'Review Date' column if it exists
    if 'Review Date' in df.columns:
        df['Review Date'] = df['Review Date'].apply(format_date)
    
    # Clean special characters from all text columns
    for col in df.select_dtypes(include=['object']).columns:
        if col != 'Review Date':
            df[col] = df[col].apply(clean_text)
            
    return df