# File-size-summarization
A script to provide excel containing list of files greater than your defined size for list of defined folders 

Program to provide excel of files with size greater than specified size in list of specified folders, with file size, extension.

```folders = [r'C:\\Windows',r'D:\\', r'E:\\']```
'D:\Big file list.xlsx'

folders = [r'C:\\Windows',r'D:\\', r'E:\\']
writer = pd.ExcelWriter(r'D:\Big file list.xlsx', engine= 'xlsxwriter')

for i in folders:
    name = 'Files at ' + i.replace('\\','').replace(':','')
    df = folder_files(folder = i, size = 200).sort_values('Size - MB', ascending=False,inplace=True)
    df.to_excel(writer, name, index = False)

writer.save()
