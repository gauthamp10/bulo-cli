# Traverse Filesystem
import os
import json
import time
import click
from pathlib import Path
from file_stats import *
from http.server import HTTPServer, BaseHTTPRequestHandler

def get_file_info(__file__):
    file_name=__file__
    file_access_time=time.ctime(os.path.getatime(__file__))
    file_modified_time=time.ctime(os.path.getmtime(__file__))
    file_change_time=time.ctime(os.path.getctime(__file__))
    file_size=os.path.getsize(__file__)
    file_extension=str(Path(__file__).suffixes)
    return(file_name,file_size,file_extension)

def get_all_files(path):
    file_list=list()    
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

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

        
@click.command()
#@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--path', default='', help='To specify the path to traverse')
@click.option('--serve', default='', help='To serve it over a specified port')
def cli(path,serve):
    if path:
        file_list=get_all_files(path) 
        for item in file_list:
                name,size,extension=get_file_info(item)
                do_ops(name,int(size),extension)
        print(read_json())
    elif path and server:
        click.echo("Hai Cooper")
    else:
        click.echo("You're awesome")




cli()





