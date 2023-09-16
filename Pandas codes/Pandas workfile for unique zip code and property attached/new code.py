import pandas as pd

# Load the CSV file
file_path = r'C:\Users\admin\OneDrive\Desktop\pandas coa workfile 17082023\coa.csv'
df = pd.read_csv(file_path)

# Group by values in column B and collect unique values from column D
result = df.groupby('Number')['Subsidiary'].unique().reset_index()

# Create a new DataFrame to hold the result
result_df = pd.DataFrame(result, columns=['Number', 'Subsidiary'])

# Write the result to an Excel file
output_file = r'C:\Users\admin\OneDrive\Desktop\pandas coa workfile 17082023\unique_subsidiaries.xlsx'
result_df.to_excel(output_file, index=False)
