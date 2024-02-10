#include <iostream>
#include <cstdlib> // Para la función system
#include <windows.h>

class VerificadorPython {
public:
    bool pythonInstalado() {
        // Intenta ejecutar el comando "python --version"
        int result = system("python --version");

        // Si el resultado es diferente de 0, significa que no se pudo ejecutar el comando
        if (result != 0) {
            return  MessageBox(NULL, "Todo listo para empezar", "INFO", MB_OK | MB_ICONINFORMATION);
        }

        // Python está instalado
        return true;
    }
};

int main() {
    VerificadorPython verificador;

    if (verificador.pythonInstalado()) {
        // Comando para ejecutar un archivo de Python (reemplaza "run.py" con tu nombre de archivo)
        const char* comando = "python run.py";

        // Ejecutar el comando
        int resultado = system(comando);

        // Verificar si la ejecución fue exitosa
        if (resultado == 0) {
           
            std::cout << "El archivo de Python se ejecutó correctamente." << std::endl;
        } else {
            std::cout << "Ocurrió un error al ejecutar el archivo de Python." << std::endl;
        }
    } else {
        MessageBox(NULL, "Hola, este es un mensaje de ejemplo.", "Mensaje", MB_OK | MB_ICONINFORMATION);;
    }

    return 0;
}

