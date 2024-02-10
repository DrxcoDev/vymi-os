import os
import time
import colorama
import subprocess
colorama.init()

name_file = input("")
os.system("cls")

print(colorama.Fore.YELLOW + "[Vymi console || 2024 Copyright || v.1.0]")
while True:
    root = input("~ User $ ")

    if root == "!clear":
        os.system("cls")
        time.sleep(1)

    elif root == "!exit" or root == "!quit":
        quit()

    elif root == "!new cmd":
        if os.path.exists("src/x86_64/env/util/NewCmd.exe"):
            subprocess.run([r"C:/Users/Soft/Documents/Py/src/x86_64/env/util/NewCmd.exe"], shell=True)
        else:
            os.system("g++ src/x86_64/env/util/NewCmd.cpp -o src/x86_64/env/util/NewCmd.exe")
    
    
    elif root == "!create file":
        extension_file = input("Extension from the file: ")
        time.sleep(1)
        name_file = input("Name from the file: ")
        time.sleep(1)
        file_repo = input("Save on [Desktop] [Documents] [Downloads] [3D Objects] [Images] [Music] [Video]: ")
        default_about = input("Enter the about: ")
        
        nf = open(f"src/x86_64/local/disk/{file_repo}/{name_file}.{extension_file}", "w")
        nf.writelines(f"{default_about}")
        nf.close()

        print(f"File created how {name_file}{extension_file} and save on {file_repo}")
    
    elif root == "!remove file":
        extension_file = input("Extension from the file: ")
        time.sleep(1)
        name_file = input("Name from the file: ")
        time.sleep(1)
        file_repo = input("Remove on [Desktop] [Documents] [Downloads] [3D Objects] [Images] [Music] [Video]: ")

        if os.path.exists:
            os.remove(f"src/x86_64/local/disk/{file_repo}/{name_file}.{extension_file}")
        else: 
            print("There not a file")


    else:
        print(f"No se encuentra el comando '{root}'")
        

