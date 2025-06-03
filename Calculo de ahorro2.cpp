#include <stdio.h>
#include <math.h>
#include <conio.h>
//Juan Diego Castro Escobar 37A
int main() {
    // Datos
    double ingresoMensual = 15000; // Ingreso mensual
    double interes = 0.037; // Interés mensual
    int years = 15; // Años
    int meses = years * 12; // Total meses
    
    // Cálculo
    double resultado = ingresoMensual * ((pow(1 + interes, meses) - 1) / interes);
    
    // Salida
    printf("El total de dinero ahorrado en %d años con ingresos mensuales de %.2f pesos ", years, ingresoMensual);
    printf("con un interes mensual del 3.7%% es: %.2f\n", resultado);
    
    getch(); // Espera
    return 0; // Fin
}

