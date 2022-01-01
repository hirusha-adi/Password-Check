import platform
from os import getcwd, listdir, name

import flask

from pwdcheck.server import app, PWD_LIST_CHECK, all_passwords_count

# Show an ASCII Art
# Taken from `figlet`
print(r"""
            ____  ____   ____ 
            |  _ \/ ___| / ___|
            | |_) \___ \| |    
            |  __/ ___) | |___ 
            |_|   |____/ \____|
        Password Strength Checker
        
""")

# To support both windows and linux+mac
SLASH = "\\"
if name == 'posix':
    SLASH = "/"

    # This information is not available for windows
    pt = platform.uname()
    print(f"""+ System Info -
    * System: {pt.system}
    * Node: {pt.node}
    * Release: {pt.release}
    * Version: {pt.version}
    * Machine: {pt.machine}""")
    print("\n")

# Display the versions
print(f"""+ Other Info -
    * Python3 Version: {platform.python_version()}
    * Flask version: {flask.__version__}""")
print("\n")

# Display the available password lists ( in `pwdcheck/passwordlists` directory`)
# these files should end with a `.txt` or `.passwords` file extention
passwords_dir = f"{getcwd()}{SLASH}pwdcheck{SLASH}passwordlists{SLASH}"
password_lists = listdir(passwords_dir)
if int(len(password_lists)) != 0:  # if there are no files available in the directory
    count = 1
    print("+ Password Lists -", "\n    * Total:", len(password_lists))
    for fileName in password_lists:
        if (fileName.lower().endswith("txt")) or (fileName.lower().endswith("passwords")):
            print(f"    {count}: {fileName}")
        count += 1
    print("\n")

# Display the amount of total loaded passwords from locally available password lists; will print nothing if 0
if PWD_LIST_CHECK == True:
    print("+ Loaded all the passwords -",
          "\n    * Count:", all_passwords_count)
    print("\n")

app.run('0.0.0.0', port=6969)
