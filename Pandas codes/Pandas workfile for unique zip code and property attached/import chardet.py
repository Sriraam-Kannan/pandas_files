import chardet

with open('C:\Users\admin\OneDrive\Desktop\pandas coa workfile 17082023\coa list.csv', 'rb') as f:
    result = chardet.detect(f.read())

df = pd.read_csv('C:\Users\admin\OneDrive\Desktop\pandas coa workfile 17082023\coa list.csv', encoding=result['encoding'])