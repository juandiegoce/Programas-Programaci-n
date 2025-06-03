#include <conio.h>
#include <stdio.h>
//Juan Diego Castro Escobar --- Area de un triangulo

int main() {
    float base, altura, area; //declara variables tipo flotante
    char opcion = 's'; //
    
    while(opcion != 'n') {
        printf("Ingresa la base del triangulo: ");
        scanf("%f", &base); //le la base
    
        printf("Ingresa la altura del triangulo: ");
        scanf("%f", &altura); //le la altura
        
        area = base * altura / 2; //hace la operacion
        printf("El area del triangulo es: %.2f\n", area);
        
        printf("Quieres volver a calcular el area de un triangulo? (s)si (n)no: "); //pide si quieres volver a calcular
        scanf(" %c", &opcion);  
    }
    
    getch();
    return 0;
}
