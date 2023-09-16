import pandas as pd

excel_file_path = r'C:\Users\admin\OneDrive\Desktop\pandas workfile 18082023\Book1.xlsx'
df = pd.read_excel(excel_file_path)


grouped = df.groupby("Account name")["Int ID"].apply(list).reset_index()


grouped.columns = ["Account Name", "Attached Subsidiaries"]

output_excel_path = r'C:\Users\admin\OneDrive\Desktop\pandas workfile 18082023\result.xlsx'
grouped.to_excel(output_excel_path, index=False)

print("Ok")
