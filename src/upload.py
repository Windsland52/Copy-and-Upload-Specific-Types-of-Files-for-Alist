# -*- coding: utf-8 -*-
import os,json,shutil

print("""--------THANKS FOR USING TOOL WRITED BY Winds_Land!--------
This tool enables the copy of specific types of files in the
current folder and works with alist to upload them to the netdisk.
I'm a freshman in github, please give me more advice.
Contact me:
- wind_land@foxmail.com
- https://space.bilibili.com/166729477
""")

# get current work directory -> str
work_path = os.getcwd()
print("Current Work Directory:\n", work_path)
# load config with 'utf-8'
with open("./config.json", 'r', encoding='utf-8') as json_file:
    config = json.load(json_file)
print("Loading config...\n")

# find unuploaded files
unupload_file, lst = [], []
all_all_file = os.walk(work_path)
for path,dir,file in all_all_file:
    for file_name in file:
        # find specific type(s) of files
        if '.' in file_name and file_name.split('.')[-1] in config['save_file_type']:
            lst.append(os.path.join(os.path.relpath(path),file_name))
            if os.path.join(os.path.relpath(path),file_name) not in config['uploaded_list']:
                unupload_file.append(os.path.join(os.path.relpath(path),file_name))

# copy files
if lst:
    print("Find file(s) whose type is {}:".format(config['save_file_type']))
    # copy files local
    for file in lst:
        print(file)
        os.makedirs(os.path.join(os.pardir,config['save_directory_name'],os.path.dirname(file)), \
                    exist_ok=True)
        shutil.copy2(file, os.path.join(os.pardir,config['save_directory_name'], file))
    
    # upload files by alist
    for file in lst:
        os.makedirs(os.path.join(config["alist_path"],os.path.dirname(file)), \
                    exist_ok=True)
        shutil.copy2(file,os.path.join(config["alist_path"], file))
    print("Copy files finished.\n")

    if unupload_file:
        print("Find unupload file(s):")
        for file in unupload_file:
            config['uploaded_list'].append(file)
            print(file)
        # modify config
        with open('./config.json', 'w', encoding='utf-8') as json_file:
            json.dump(config,json_file,indent=2)
        print("Config modified.")
else:
    print("No File.")
  
os.system("exit")
