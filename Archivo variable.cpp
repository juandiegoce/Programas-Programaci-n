#include <stdio.h>
#include <conio.h>
#define MAX_SIZE 10000
//Juan Diego Castro Escobar 37A --- Se pide un archivo con subfijo "txt" y lee el archivo
int main() {
    char nombre_archivo[100]; //es el nombre del archivo con maximo de caracteres
    char contenido[MAX_SIZE] = {0};
    FILE *archivo;
    int i = 0;
    printf("Ingrese el nombre del archivo de texto (ej. 'archivo.txt'): ");
    scanf("%99s", nombre_archivo);
    archivo = fopen(nombre_archivo, "r"); //se busca el archivo en la carpeta en donde esta el programa
    if (archivo == NULL) {
        printf("\nError: No se pudo abrir el archivo '%s'\n", nombre_archivo);
        printf("Asegurese de que el archivo existe y esta en el mismo directorio.\n"); //error si el archivo no tiene el directorio del programa
        getch();
        return 1;
    }
    printf("\nLeyendo archivo...\n");
    while (i < MAX_SIZE - 1 && (contenido[i] = fgetc(archivo)) != EOF) {
        i++;
    }
    contenido[i] = '\0';
    fclose(archivo);
    printf("\nContenido del archivo:\n");
    printf("----------------------------------------\n");
    printf("%s", contenido);
    printf("\n----------------------------------------\n"); //entre estas lineas se muestra el archivo
    printf("\nEl archivo se ha guardado correctamente en la variable.\n");
    printf("Presione cualquier tecla para salir...");
    getch();
    return 0;
}
