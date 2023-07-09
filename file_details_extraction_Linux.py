import os
import pandas as pd

def get_folder_file_details(folder):
    file_details = []
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.basename(file_path)
            folder_address = os.path.dirname(file_path)
            file_size = os.path.getsize(file_path)
            
            file_details.append((file_name, folder_address, file_size))
    
    return file_details

def write_file_details(file_details, output_file):
    with open(output_file, 'w') as f:
        f.write(f"File_Name,Folder_Address,File_Size\n")
        for file_name, folder_address, file_size in file_details:
            f.write(f"{file_name},{folder_address},{file_size}\n")

#### Example of using
folder_path = '/root'  # Replace with the desired folder path
# output_file = 'file_details.txt'  # Replace with the desired output file path

details = get_folder_file_details(folder_path)
# write_file_details(details, output_file)

df = pd.DataFrame(details).sort_values(by='File_Size', ascending=False,inplace=True)
df.to_csv('file_details.csv', index=False)
