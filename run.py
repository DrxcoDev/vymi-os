import platform
import os
import time
import psutil

# -*-*-*-*-*-*

# BIOS

# -*-*-*-*-*-*

def obtener_arquitectura():
    sistema_operativo = platform.architecture()[0]
    

    if sistema_operativo == "64bit":
        print(f"Os is: {sistema_operativo}%, BIOS arch = Python v 3.0")
        
        data = open("./src/x86_64/datatime.data", "w")
        data.writelines("%Bit = x64 ;")
        data.close()

    elif sistema_operativo == "86bit":
        print(f"Os is: {sistema_operativo}%, BIOS arch = Python v 3.0")

        data = open("./src/x86_64/datatime.data", "w")
        data.writelines("%Bit = x86_64 ;")
        data.close()
        
    elif sistema_operativo == "32bit":
        print(f"Os is: {sistema_operativo}%, BIOS arch = Python v 3.0")

        data = open("./src/x32/datatime.data", "w")
        data.writelines("%Bit = x32 ;")
        data.close()
    else:
        print(f"Succes {sistema_operativo}!! 100%")

        data = open("./src/x32/datatime.data", "w")
        data.writelines("!Bit = x32 ;")
        data.close()
        
def obtener_ram():
    with open("./src/x86_64/datatime.data", 'r') as archivo:
            lineas = archivo.readlines()
            for numero_linea, linea in enumerate(lineas, start=1):
                if "%Bit = x64 ;" in linea:

                     # Obtener información sobre la memoria RAM
                        mem = psutil.virtual_memory()
                        
                        # Convertir los valores de bytes a megabytes para mayor legibilidad
                        total_ram = mem.total / (1024 ** 2)  # Convertir bytes a megabytes

                        data = open("./src/x86_64/ram.data", "w")
                        data.writelines(f"Total RAM: {total_ram:.2f} %%")
                        data.close()
   

def bios():
    time.sleep(2)
    print(obtener_arquitectura())
    os.system("cls")
    time.sleep(3)
    obtener_ram()
    os.system("python src/x86_64/x86_64.py")

bios()