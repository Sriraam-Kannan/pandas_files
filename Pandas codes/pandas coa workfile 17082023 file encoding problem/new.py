import pandas as pd

# Load the CSV file
file_path = r'C:\Users\admin\OneDrive\Desktop\pandas coa workfile 17082023\file.csv'
df = pd.read_csv(file_path)

result = df.groupby('Number')['Subsidiary'].apply(list).reset_index()

# Convert subsidiary lists to strings
result['Subsidiary'] = result['Subsidiary'].apply(', '.join)

# Create a new DataFrame to hold the result
result_df = pd.DataFrame(result, columns=['Number', 'Subsidiary'])

# Write the result to an Excel file
output_file = r'C:\Users\admin\OneDrive\Desktop\pandas coa workfile 17082023\account_subsidiaries_summary.xlsx'
result_df.to_excel(output_file, index=False)
