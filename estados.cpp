#include <stdio.h>
#include <conio.h>
#include <string.h>
//Juan Diego Castro Escobar 37A
int main() {
    char texto[100]; // Almacena el texto ingresado
    char estado[3] = "S1"; // Estado inicial
    int valido = 1;  // Indica si el texto es válido
    
    printf("Ingresa el texto: ");
    scanf("%s", texto); // Lee el texto
    
    for(int i = strlen(texto)-1; i >= 0; i--) { // Recorre el texto al revés
        char letra = texto[i]; // Letra actual
        char nuevo_estado[3] = ""; // Nuevo estado
        
        // Transiciones del autómata
        if(!strcmp(estado, "S1") && letra == 'a') strcpy(nuevo_estado, "S2");
        else if(!strcmp(estado, "S2")) {
            if(letra == 'a') strcpy(nuevo_estado, "S2");
            else if(letra == 'c') strcpy(nuevo_estado, "S4");
            else if(letra == 'b') strcpy(nuevo_estado, "S1");
        }
        else if(!strcmp(estado, "S3")) {
            if(letra == 'b') strcpy(nuevo_estado, "S4");
            else if(letra == 'a') strcpy(nuevo_estado, "S1");
        }
        else if(!strcmp(estado, "S4")) {
            if(letra == 'd') strcpy(nuevo_estado, "S3");
            else if(letra == 'a') strcpy(nuevo_estado, "S5");
        }
        
        if(strlen(nuevo_estado)) { // Si hay un nuevo estado
            strcpy(estado, nuevo_estado); // Actualiza el estado
            printf("%c -> Cambio a estado %s\n", letra, estado);
        } else { // Transición no válida
            printf("%c -> Transicion no valida desde %s\n", letra, estado);
            valido = 0; // Marca como inválido
            break;
        }
    }
    
    if(valido) { // Si es válido
        printf("\nEl texto es valido. Estado final: %s\n", estado);
    } else { // Si es inválido
        printf("\nEl texto es invalido. Se quedo en: %s\n", estado);
    }
    
    getch(); // Espera
    return 0; // Fin
}

