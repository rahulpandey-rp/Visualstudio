import sys,os

root = "/home/rahul/Visualstudio"
path = os.path.join(root, "python")

for roots,dirs,files in os.walk(root):
    for file in files:
        file_path = (os.path.join(roots,file)).split("/")
        print(f"{'-->'.join(file_path[:-1])} : {file_path[-1]}")