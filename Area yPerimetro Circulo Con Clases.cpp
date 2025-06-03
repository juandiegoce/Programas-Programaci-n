#include <conio.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
//Juan Diego Castro Escobar 37A
class Circulo { // Clase para representar un c�rculo
    private:
        float pi = 3.1416; // Valor de pi
    public: 
        float radio; // Radio del c�rculo
        
    float Area() { // Calcula el �rea
        return pi * (radio * radio);
    }
    
    float Perimetro() { // Calcula el per�metro
        return 2 * pi * radio;
    }
};

int main() {
    Circulo circulo; // Instancia de la clase Circulo
    char opcion[3]; 
    int salir = 0; // Controla la salida del bucle

    printf("Ingresa el radio del circulo: ");
    scanf("%f", &circulo.radio); // Lee el radio del c�rculo
    
    while(!salir) { // Bucle para seleccionar opci�n
        printf("\nSelecciona que deseas calcular:\n(A)Area\n(P)Perimetro\n(S)Salir\n");
        scanf("%s", opcion); // Lee la opci�n del usuario
        opcion[0] = toupper(opcion[0]); // Convierte a may�scula
        
        if(strcmp(opcion, "A") == 0) { // Si opci�n es A
            printf("El area del circulo es: %.2f\n", circulo.Area());
        }
        else if(strcmp(opcion, "P") == 0) { // Si opci�n es P
            printf("El perimetro del circulo es: %.2f\n", circulo.Perimetro());
        }
        else if(strcmp(opcion, "S") == 0) { // Si opci�n es S
            salir = 1; // Cambia salir a 1 para terminar
        }
        else { // Opci�n no v�lida
            printf("Opcion no valida. Intente nuevamente.\n");
        }
    }
    
    getch(); // Espera a que el usuario presione una tecla
    return 0; // Fin del programa
}

