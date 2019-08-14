import json

# to read from json
def read_json():
    with open("db.json") as data_file:
	    data = json.load(data_file)
    return data

#to write to db.json
def write_json(data):
    with open("db.json",'w+') as file_data:
        json.dump(data,file_data)

# to find most common from a list
def most_common(lst):
    return max(set(lst), key=lst.count)

# to maintain statistics of post data recieved.
def do_ops(__newfilepath__,__newfilesize__,__newext__):
    data = read_json()
    #number of files recieved
    file_count = int(data['no_of_files'])
    file_count=file_count+1

    #maximum file size and path
    max_file_size=data['max_file_size']['size']
    max_file_path=str(data['max_file_size']['path'])
    print(__newfilesize__)
    if(int(max_file_size)<=__newfilesize__):
        max_file_size=int(__newfilesize__)
        max_file_path=__newfilepath__

    #average file size
    file_size_sum=int(data['file_size_sum'])
    file_size_sum=file_size_sum+__newfilesize__
    avg_file_size=file_size_sum/file_count

    #file extensions
    file_extensions=list(data['extensions'])
    file_extensions.append(__newext__)
    extension_set=list(set(file_extensions))
    print(file_extensions)
    #most frequent extension occurance
    ext_count=0
    for i in file_extensions:
        if i==most_common(file_extensions):
            ext_count=ext_count+1
    freq_ext=most_common(file_extensions)
    freq_ext_count=ext_count

    #list of latest 10 file paths
    latest_paths=data['latest_file_paths']
    list_len=len(latest_paths)
    if(list_len == 10):
        latest_paths[9]=__newfilepath__
    else:
        latest_paths.append(__newfilepath__)

    data['no_of_files']=file_count
    data['max_file_size']['size']=max_file_size
    data['max_file_size']['path']=max_file_path
    data['avg_file_size']=avg_file_size
    data['extensions']=extension_set
    data['freq_extension']['extension']=freq_ext
    data['freq_extension']['count']=freq_ext_count
    data['latest_file_paths']=latest_paths
    data['file_size_sum']=file_size_sum
    
#Dummy data to populate
    '''data=read_json()
    data['no_of_files']=0
    data['max_file_size']['size']=0
    data['max_file_size']['path']=''
    data['avg_file_size']=0
    data['freq_extension']['extension']=''
    data['freq_extension']['count']=0
    data['latest_file_paths']=[]
    data['extensions']=[]
    data['file_size_sum']=0'''
    
    write_json(data)




