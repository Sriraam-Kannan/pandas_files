import pandas as pd
file_path = r'C:\Users\admin\OneDrive\Desktop\pandas coa workfile 17082023\file.csv'
df = pd.read_csv(file_path, engine='openpyxl')
result = df.groupby('Number')['Subsidiary'].apply(list).reset_index()
output_file = r'C:\Users\admin\OneDrive\Desktop\pandas coa workfile 17082023\result.xlsx'
result.to_excel(output_file, index=False, engine='xlsxwriter')
