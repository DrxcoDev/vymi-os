import time
import psutil
import re
import os

# -*-*-*-*-*-*

# Configuracion del rendimiento por el BIT de la BIOS

# -*-*-*-*-*-*

def respuesta_en_base_a_ram():
    with open("src/x86_64/ram.data", 'r') as archivo:
            lineas = archivo.readlines()
            for numero_linea, linea in enumerate(lineas, start=1):
                valores_numericos = re.findall(r'\b\d+\b', linea)
                if valores_numericos:
                    print(f"Valores numéricos encontrados en la línea {numero_linea}: {valores_numericos}")


                    # Obtener la cantidad de memoria RAM disponible en el sistema
                    mem = psutil.virtual_memory()
                    ram_disponible = mem.available / (1024 ** 2)  # Convertir bytes a megabytes
                    
                    # Determinar el retraso en base a la cantidad de RAM disponible
                    if ram_disponible < 1024:  # Menos de 1GB de RAM
                        retraso = 2  # Retraso más largo
                    elif ram_disponible < 4096:  # Entre 1GB y 4GB de RAM
                        retraso = 1  # Retraso moderado
                    else:  # Más de 4GB de RAM
                        retraso = 0.5  # Retraso más corto
                    
                    # Simular un retraso en la respuesta
                    time.sleep(retraso)
                    
                    data = open("src/x86_64/retard.data", "w")
                    data.writelines(f"{retraso}")
                    data.close()

# INIT
                    

respuesta_en_base_a_ram()
os.system("python src/x86_64/env/cmd.py")

