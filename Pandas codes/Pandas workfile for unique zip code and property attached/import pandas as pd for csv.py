import pandas as pd
file_path = r'C:\Users\admin\OneDrive\Desktop\Pandas workfile\pandas workfile.csv'
df = pd.read_csv(file_path, engine='openpyxl')
result = df.groupby('City Code')['Property'].apply(list).reset_index()
output_file = r'C:\Users\admin\OneDrive\Desktop\Pandas workfile\pandas result.csv'
result.to_excel(output_file, index=False, engine='openpyxl')
