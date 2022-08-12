# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 2018
@author: jupihes
Program to provide excel of files with size greater than specified size in list of specified folders, with file size, extension.
"""
import pandas as pd
import os

def folder_files(folder = r'C:\\', size = 200):
    folder_size = 0
    rows_list = []
    for (path, dirs, files) in os.walk(folder):
        # temp = ''
        
        for file in files:
            #dict1 = {}
            filename = os.path.join(path, file)
            if os.path.getsize(filename)/1000./1000 > size:
    #            temp = filename + '\t' + str(os.path.getsize(filename)/1000./1000) + '\t'\
    #            + str(filename.split('.')[-1]) +'\n'
    #            file1.write(temp)
    
                folder_size += os.path.getsize(filename)
                
                temp_list = [filename, str(os.path.getsize(filename)/1000./1000),\
                str(os.path.splitext(filename)[-1])]
                rows_list.append(temp_list)
            
           
    #print("Folder = %0.1f MB" % (folder_size/(1000*1000.0)))
    print(f"Sum greater than {size} MB files at folder {folder} = {folder_size/(1000*1000.0):0.1f} MB")
    df = pd.DataFrame(rows_list,columns= ['File/Folder Name','Size - MB','File type'])
    return df

folders = [r'C:\\Windows',r'D:\\', r'E:\\']
writer = pd.ExcelWriter(r'D:\Big file list.xlsx', engine= 'xlsxwriter')

for i in folders:
    name = 'Files at ' + i.replace('\\','').replace(':','')
    df = folder_files(folder = i, size = 200).sort_values('Size - MB', ascending=False,inplace=True)
    df.to_excel(writer, name, index = False)

writer.save()
