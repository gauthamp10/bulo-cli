# Traverse Filesystem
import os
import json
import time
from pathlib import Path
from file_stats import *

def get_file_info(__file__):
    file_name=__file__
    file_access_time=time.ctime(os.path.getatime(__file__))
    file_modified_time=time.ctime(os.path.getmtime(__file__))
    file_change_time=time.ctime(os.path.getctime(__file__))
    file_size=os.path.getsize(__file__)
    file_extension=str(Path(__file__).suffixes)
    return(file_name,file_size,file_extension)

def get_all_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            print( os.path.join(root, file))

def get_filesNdir(path):
        folders = []
        files = []
        for entry in os.scandir(path):
            if entry.is_dir():
                folders.append(entry.path)
            elif entry.is_file():
                files.append(entry.path)
        print('Folders:')
        print(folders)
        print('Files:')
        print(files)

def get_dir_size(path):
        total_size = 0
        start_path = str(path)  # To get size of current directory
        for path, dirs, files in os.walk(start_path):
                for f in files:
                        fp = os.path.join(path, f)
                        total_size += os.path.getsize(fp)
        return(str(total_size))        

        
'''get_all_files('/home/bulo98/Desktop/')        
get_filesNdir('/home/bulo98/')
get_file_info('/home/bulo98/intro/wallpaper.jpg')
get_dir_size("/home/bulo98/Music")'''

file = input("Enter the full file path:")
name,size,extension=get_file_info(file)
do_ops(name,int(size),extension)