#  Write a python program to create a directory and subdirectory. It should print the current working directory path 
# and list of names of files present in the given directory.

import os
os.makedirs("main_dir/sub_dir")  # Create directory and subdirectory

print("Current Directory:", os.getcwd())  
print("Files in 'main_dir':", os.listdir("main_dir"))  
