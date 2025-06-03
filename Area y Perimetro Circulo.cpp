#include <stdio.h>
#include <conio.h>
//Juan Diego Castro Escobar 37A ---ara y perimetro de un circulo
#define PI 3.1416

float calcularArea(float radio) {
    return PI * (radio * radio); //calculo de area
}

float calcularPerimetro(float radio) {
    return 2 * PI * radio; //calculo de perimetro
}

int main() {
    char opcion;
    float radio;
    printf("Ingresa el radio del circulo: ");
    scanf("%f", &radio);
    do {
        printf("\nSelecciona que deseas calcular:\n(A)Area\n(P)Perimetro\n(S)Salir\n"); //pide que quieres calcular
        scanf(" %c", &opcion);
        
        if(opcion == 'a' || opcion == 'A') { //opcion A que te lleva a calcular el area
            printf("El area del circulo es: %.2f\n", calcularArea(radio));
        }
        else if(opcion == 'p' || opcion == 'P') { //opcion P que te lleva a calcular el perimetri
            printf("El perimetro del circulo es: %.2f\n", calcularPerimetro(radio));
        }
        else if(opcion == 's' || opcion == 'S') { //Se sale del programa seleccionando S
            break;
        }
        else { //no pusiste ninguna opcion
            printf("Opcion no valida\n");
        }
    } while(1);
    getch();
    return 0;
}
