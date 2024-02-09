#include <iostream>
#include <cstdlib> // Para la función system

int main() {
    // Comando para ejecutar un archivo de Python (reemplaza "script.py" con tu nombre de archivo)
    const char* comando = "python run.py";

    // Ejecutar el comando
    int resultado = system(comando);

    // Verificar si la ejecución fue exitosa
    if (resultado == 0) {
        std::cout << "El archivo de Python se ejecutó correctamente." << std::endl;
    } else {
        std::cout << "Ocurrió un error al ejecutar el archivo de Python." << std::endl;
    }

    return 0;
}
