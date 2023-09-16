import pandas as pd

file_path = r'C:\Users\admin\OneDrive\Desktop\pandas coa workfile 17082023\COA list.csv'
df = pd.read_csv(file_path)

result = df.groupby('Number')['Sub Int ID'].apply(list).reset_index()

output_file = r'C:\Users\admin\OneDrive\Desktop\pandas coa workfile 17082023\coa with sub details.csv'
result.to_csv(output_file, index=False)
