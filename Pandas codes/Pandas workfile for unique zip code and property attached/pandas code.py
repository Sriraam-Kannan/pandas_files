#py code for comparing zip code in col A,property code in Col B and Int id in col C. And result file with unique zip code and intID 
import pandas as pd

file_path = r'D:\dd\sriraam employee files\Pandas codes\Pandas workfile for unique zip code and property attached\new file.xlsx'
df = pd.read_excel(file_path)

result = df.groupby('Zip Code')['Int ID'].apply(list).reset_index()

output_file = r'D:\dd\sriraam employee files\Pandas codes\Pandas workfile for unique zip code and property attached\new.xlsx'
result.to_excel(output_file, index=False, engine='xlsxwriter')
