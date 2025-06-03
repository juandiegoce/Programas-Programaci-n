#include <stdio.h>
#include <conio.h>

int main() {
    int numeros[10]; // Arreglo para almacenar 10 números
    int i, j, temp; // Variables para iteración y temporal

    printf("Ingrese 10 valores numericos:\n");
    for(i = 0; i < 10; i++) { // Ciclo para ingresar números
        printf("Valor %d: ", i + 1);
        scanf("%d", &numeros[i]); // Lee cada número
    }

    for(i = 0; i < 9; i++) { // Ciclo para ordenar
        for(j = 0; j < 9 - i; j++) { // Comparaciones para burbuja
            if(numeros[j] > numeros[j + 1]) { // Si el número actual es mayor que el siguiente
                temp = numeros[j]; // Intercambio
                numeros[j] = numeros[j + 1];
                numeros[j + 1] = temp;
            }
        }
    }

    printf("\nLos números ordenados de forma ascendente quedarian de la siguiente manera:\n");
    for(i = 0; i < 10; i++) { // Ciclo para mostrar números ordenados
        printf("%d ", numeros[i]);
    }

    getch(); // Espera a que el usuario presione una tecla
    return 0; // Fin del programa
}

