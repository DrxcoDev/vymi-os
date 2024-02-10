#include <iostream>
#include <cstdlib> // Para la función system
#include <ctime>

int main() {
    // Obtener la hora actual
    std::time_t tiempo_actual = std::time(nullptr);
    std::tm* tiempo_descompuesto = std::localtime(&tiempo_actual);

    // Determinar si es de día o de noche
    if (tiempo_descompuesto->tm_hour >= 6 && tiempo_descompuesto->tm_hour < 18) {
        // Es de día, ejecutar la aplicación para el día
        system("src/x86_64/env/cmd.py");
    } else {
        // Es de noche, ejecutar la aplicación para la noche
        system("src/x86_64/env/cmd.py");
    }

    return 0;
    
}