import pandas as pd

# Load your Excel file into a DataFrame
df = pd.read_excel("C:/Users/Ines/Downloads/The Great Replacement-quotations (3).xlsx")

# Pivot the data to create a new DataFrame
pivot_df = df.pivot(columns='Codes', values='Comment')

# Save the pivoted data to a new Excel file or sheet
pivot_df.to_excel('"C:/Users/Ines/Downloads/The Great Replacement-quotations_pivoted.xlsx"', index=False)
