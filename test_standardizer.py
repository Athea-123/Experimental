import pandas as pd
from pyclense.standardizer import FormatStandardizer

# 1. Create a "Messy" Dataset
# We intentionally put bad formats, emojis, symbols, and weird spacing here.
data = {
    'Date': ['2023-01-01', '01/02/2023', 'Jan 3, 2023', '2023.01.04'],
    'Name': ['athea budlong', 'SARIBA ABDULA', 'kaTe aVancena', 'jynobelle'],
    'City': ['  Cagayan   de Oro  ', 'Manila  ', '  Davao', 'Cebu'],
    'ID_Code': ['User@101', 'User#102', 'User$103', 'User&104'],
    'Is_Student': ['yes', 'N', 'TRUE', '0']
}

df = pd.DataFrame(data)

print("\n" + "="*40)
print("❌ BEFORE CLEANING (MESSY DATA)")
print("="*40)
print(df)

# 2. Initialize your Standardizer
# We pass the dataframe to your class
cleaner = FormatStandardizer(df)

# 3. Run the Cleaning Methods
# We use "Method Chaining" to do everything in one go
cleaner.standardize_dates(['Date'])             # Fix dates to MM/DD/YYYY
cleaner.capitalize_names(['Name'])              # Fix names to Title Case
cleaner.fix_whitespace(['City'])                # Fix messy spaces
cleaner.remove_special_chars(['ID_Code'])       # Remove @, #, $
cleaner.standardize_booleans(['Is_Student'])    # Turn yes/no into True/False

# 4. Get the Final Data
clean_df = cleaner.get_dataframe()

print("\n" + "="*40)
print("✅ AFTER CLEANING (PYCLENSE)")
print("="*40)
print(clean_df)

# 5. Verify Data Types
print("\n--- Final Data Types ---")
print(clean_df.dtypes)