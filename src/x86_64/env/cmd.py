import os
import time
import colorama
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
        

