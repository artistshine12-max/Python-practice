# write a python programme to print the contents of a directory using the os module.search online for the function which does that
import os

# List contents of the current directory
print("Current directory contents:")
for item in os.listdir():
    print(item)

# List contents of a specific directory
directory_path = "C:/Path_Of_Some_Directory/admin"
print(f"\nContents of {directory_path}:")
try:
    for item in os.listdir(directory_path):
        print(item)
except FileNotFoundError:
    print(f"Directory {directory_path} not found")
except PermissionError:
    print(f"No permission to access {directory_path}")
