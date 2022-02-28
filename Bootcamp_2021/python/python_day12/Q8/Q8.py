import os
import re
def rename_all(dir_path, pattern, suffix):
    for filename in os.listdir(dir_path):
        result = re.match(pattern, filename)
        if(result):
            rename = filename.split(".")
            os.rename(dir_path+"/"+filename,dir_path+"/"+rename[0]+suffix+"."+rename[1])


rename_all("/home/rahul/Visualstudio/python/python_day12/Q8", "Test_file_*", "new")