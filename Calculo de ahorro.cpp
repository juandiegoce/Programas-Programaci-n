#include <stdio.h>
#include <conio.h>
#include <math.h> 
//Juan Diego castro escobar 37A
int main() {
    // Datos
    double ingresoMensual = 1000; // Ingreso mensual
    double interes = 0.03; // Interés mensual
    int years = 10; // Años
    int meses = years * 12; // Total meses
    
    // Cálculo
    double resultado = ingresoMensual * ((pow(1 + interes, meses) - 1) / interes);
    
    // Salida
    printf("El total de dinero ahorrado en %d años con ingresos mensuales de %.2f pesos ", years, ingresoMensual);
    printf("con un interes mensual del 3%% es: %.2f\n", resultado);

    getch(); // Espera
    return 0; // Fin
}

