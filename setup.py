# Setup the Password Strength Checker
# This script will download two recommended password lists to the pwdchecl/passwordlists directory

import os
import requests
print("* Starting to setup Password Strength Checker")

SLASH = "\\"
if os.name == 'posix':
    SLASH = "/"

passwords_dir = f"{os.getcwd()}{SLASH}pwdcheck{SLASH}passwordlists"

# File 1
TEN_MIL = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
print("* Starting to download: 10-million-password-list-top-1000000.txt")
r1 = requests.get(TEN_MIL).text
print("* Writing downloaded data to file")
with open(f"{passwords_dir}{SLASH}10-million-password-list-top-1000000.txt", "w", encoding="utf-8") as tenMilFile:
    tenMilFile.write(r1)
print("* Completed: 10-million-password-list-top-1000000.txt")

# File 2
q1 = input("? Do you want to download another password list? Continuing will make the program resource heavy: ")
if q1.lower().strip().startswith("y"):
    TEN_K = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/darkweb2017-top10000.txt"
    print("* Starting to download: darkweb2017-top10000.txt")
    r1 = requests.get(TEN_K).text
    print("* Writing downloaded data to file")
    with open(f"{passwords_dir}{SLASH}darkweb2017-top10000.txt", "w", encoding="utf-8") as tenMilFile:
        tenMilFile.write(r1)
    print("* Completed: darkweb2017-top10000.txt")

print("+ Completed", "\n+ You can now start the program")
