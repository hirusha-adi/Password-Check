import platform
from os import getcwd, listdir, name

import flask

from pwdcheck.server import app, PWD_LIST_CHECK, all_passwords_count

print(r"""
            ____  ____   ____ 
            |  _ \/ ___| / ___|
            | |_) \___ \| |    
            |  __/ ___) | |___ 
            |_|   |____/ \____|
        Password Strength Checker
        
""")

SLASH = "\\"
if name == 'posix':
    SLASH = "/"
    pt = platform.uname()
    print(f"""+ System Info -
    * System: {pt.system}
    * Node: {pt.node}
    * Release: {pt.release}
    * Version: {pt.version}
    * Machine: {pt.machine}""")

print("\n")

print(f"""+ Other Info -
    * Python3 Version: {platform.python_version()}
    * Flask version: {flask.__version__}""")

print("\n")

# Display the available password lists
# these files should end with a `.txt` or `.passwords` file extention
passwords_dir = f"{getcwd()}{SLASH}pwdcheck{SLASH}passwordlists{SLASH}"
password_lists = listdir(passwords_dir)
count = 1
print("+ Password Lists -", "\n    * Total:", len(password_lists))
for fileName in password_lists:
    if (fileName.lower().endswith("txt")) or (fileName.lower().endswith("passwords")):
        print(f"    {count}: {fileName}")
    count += 1

print("\n")

if PWD_LIST_CHECK == True:
    print("+ Loaded all the passwords -",
          "\n    * Count:", all_passwords_count)

print("\n")
print("\n")

app.run('0.0.0.0', port=6969)
