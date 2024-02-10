import os
import time
import colorama
import subprocess
colorama.init()


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
    else:
        print(f"No se encuentra el comando '{root}'")
        

