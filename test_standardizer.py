import pandas as pd
from pyclense.standardizer import Standardizer

# 1. Create a "Messy" Dataset
data = {
    'Date': ['2023-01-01', '01/02/2023', 'Jan 3, 2023', '2023.04.05'],
    'Name': ['athea budlong', 'SARIBA ABDULA', 'kaTe aVancena', 'jynobelle JacoBo'],
    'City': ['  Cagayan   de Oro  ', 'Manila  ', '  Davao', 'Cebu'],
    'ID_Code': ['User@101', 'User#102', 'User$103', 'User&104'],
    'Is_Student': ['yes', 'N', 'TRUE', '0']
}

df = pd.DataFrame(data)

print("\n" + "="*40)
print("❌ BEFORE CLEANING")
print("="*40)
print(df)

# 2. Initialize your Standardizer
cleaner = Standardizer(df)

# 3. Run All Methods
cleaner.standardize_dates(['Date'])
cleaner.capitalize_names(['Name'])
cleaner.fix_whitespace(['City'])
cleaner.remove_special_chars(['ID_Code'])
cleaner.standardize_booleans(['Is_Student'])

# 4. Get the Final Data
clean_df = cleaner.get_dataframe()

print("\n" + "="*40)
print("✅ AFTER CLEANING (PYCLENSE)")
print("="*40)
print(clean_df)
print("\n" + "="*40)