#include <conio.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
//Juan Diego Castro Escobar 37A
class Circulo { // Clase para representar un círculo
    private:
        float pi = 3.1416; // Valor de pi
    public: 
        float radio; // Radio del círculo
        
    float Area() { // Calcula el área
        return pi * (radio * radio);
    }
    
    float Perimetro() { // Calcula el perímetro
        return 2 * pi * radio;
    }
};

int main() {
    Circulo circulo; // Instancia de la clase Circulo
    char opcion[3]; 
    int salir = 0; // Controla la salida del bucle

    printf("Ingresa el radio del circulo: ");
    scanf("%f", &circulo.radio); // Lee el radio del círculo
    
    while(!salir) { // Bucle para seleccionar opción
        printf("\nSelecciona que deseas calcular:\n(A)Area\n(P)Perimetro\n(S)Salir\n");
        scanf("%s", opcion); // Lee la opción del usuario
        opcion[0] = toupper(opcion[0]); // Convierte a mayúscula
        
        if(strcmp(opcion, "A") == 0) { // Si opción es A
            printf("El area del circulo es: %.2f\n", circulo.Area());
        }
        else if(strcmp(opcion, "P") == 0) { // Si opción es P
            printf("El perimetro del circulo es: %.2f\n", circulo.Perimetro());
        }
        else if(strcmp(opcion, "S") == 0) { // Si opción es S
            salir = 1; // Cambia salir a 1 para terminar
        }
        else { // Opción no válida
            printf("Opcion no valida. Intente nuevamente.\n");
        }
    }
    
    getch(); // Espera a que el usuario presione una tecla
    return 0; // Fin del programa
}

