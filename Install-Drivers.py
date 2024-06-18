import os

folder_path = 'Path'


for file_name in os.listdir(folder_path):
    if file_name.endswith('.inf'):  
        file_path = os.path.join(folder_path, file_name)
       
        os.system(f'dism /online /add-driver /driver:"{file_path}"')
        print(f'Installing driver: {file_name}')
