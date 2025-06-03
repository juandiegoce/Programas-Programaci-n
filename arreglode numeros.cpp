#include <stdio.h>
#include <conio.h>

int main() {
    int numeros[10]; // Arreglo para almacenar 10 n�meros
    int i, j, temp; // Variables para iteraci�n y temporal

    printf("Ingrese 10 valores numericos:\n");
    for(i = 0; i < 10; i++) { // Ciclo para ingresar n�meros
        printf("Valor %d: ", i + 1);
        scanf("%d", &numeros[i]); // Lee cada n�mero
    }

    for(i = 0; i < 9; i++) { // Ciclo para ordenar
        for(j = 0; j < 9 - i; j++) { // Comparaciones para burbuja
            if(numeros[j] > numeros[j + 1]) { // Si el n�mero actual es mayor que el siguiente
                temp = numeros[j]; // Intercambio
                numeros[j] = numeros[j + 1];
                numeros[j + 1] = temp;
            }
        }
    }

    printf("\nLos n�meros ordenados de forma ascendente quedarian de la siguiente manera:\n");
    for(i = 0; i < 10; i++) { // Ciclo para mostrar n�meros ordenados
        printf("%d ", numeros[i]);
    }

    getch(); // Espera a que el usuario presione una tecla
    return 0; // Fin del programa
}

