#include <stdio.h>
#include <conio.h>
#include <windows.h>
//JUAN DIEGO CASTRO ESCOBAR 37A
class Lavadora {
    public:
        char plan[20];
        int contador, ciclo;

        void off() {
            printf("Apagando lavadora\n");
        }

        void idle() {
            printf("(1) Regular\n(2) Delicado\n(3) Super Delicado\n(4) Apagar\n");
            printf("Ingrese el tipo de lavado que desea realizar: ");
            scanf("%d", &ciclo);

            if (ciclo == 1) {
                printf("La lavadora esta encendida.\n");
                strcpy(plan, "regular");
                printf("Ahora el plan de lavado es %s\n", plan);
                soak(1);
            }
            if (ciclo == 2) {
                printf("La lavadora esta encendida.\n");
                strcpy(plan, "delicado");
                printf("Ahora el plan de lavado es %s\n", plan);
                rinse(2);
            }
            if (ciclo == 3) {
                printf("La lavadora esta encendida.\n");
                strcpy(plan, "super delicado");
                printf("Ahora el plan de lavado es %s\n", plan);
                rinse(3);
            }
            if (ciclo == 4) {
                off();
            }
        }

        void soak(int ciclo) {
            if (ciclo == 1) {
                printf("La lavadora ha comenzado a remojar la ropa\n");
                printf("Remojando la ropa..\n");

                contador = 0;

                for (int i = 0; i < 5; ++i) {
                    printf("%d\n", contador + 1);
                    contador++;
                    Sleep(1000);
                }

                printf("Remojado terminado.\n");
                rinse(1);
            }
        }

        void rinse(int ciclo) {
            if (ciclo == 1) {
                printf("La lavadora ha comenzado a enjuagar la ropa\n");
                printf("Enjuagando la ropa..\n");

                contador = 0;

                for (int i = 0; i < 5; ++i) {
                    printf("%d\n", contador + 1);
                    contador++;
                    Sleep(1000);
                }

                printf("Enjuagado terminado.\n");
                drain(1);
            }
            if (ciclo == 2) {
                printf("La lavadora ha comenzado a enjuagar la ropa\n");
                printf("Enjuagando la ropa..\n");

                contador = 0;

                for (int i = 0; i < 5; ++i) {
                    printf("%d\n", contador + 1);
                    contador++;
                    Sleep(1000);
                }

                printf("Enjuagado terminado.\n");
                drain(2);
            }
            if (ciclo == 3) {
                printf("La lavadora ha comenzado a enjuagar la ropa\n");
                printf("Enjuagando la ropa..\n");

                contador = 0;

                for (int i = 0; i < 5; ++i) {
                    printf("%d\n", contador + 1);
                    contador++;
                    Sleep(1000);
                }

                printf("Enjuagado terminado.\n");
                drain(3);
            }
        }

        void drain(int ciclo) {
            if (ciclo == 1) {
                printf("Comenzando a drenar el agua.\n");
                printf("Drenando agua..\n");

                contador = 0;

                for (int i = 0; i < 5; ++i) {
                    printf("%d\n", contador + 1);
                    contador++;
                    Sleep(1000);
                }

                printf("Drenado de agua terminado.\n");
                dry(1);
            }
            if (ciclo == 2) {
                printf("Comenzando a drenar el agua.\n");
                printf("Drenando agua..\n");

                contador = 0;

                for (int i = 0; i < 5; ++i) {
                    printf("%d\n", contador + 1);
                    contador++;
                    Sleep(1000);
                }

                printf("Drenado de agua terminado.\n");
                dry(2);
            }
            if (ciclo == 3) {
                printf("Comenzando a drenar el agua.\n");
                printf("Drenando agua..\n");

                contador = 0;

                for (int i = 0; i < 5; ++i) {
                    printf("%d\n", contador + 1);
                    contador++;
                    Sleep(1000);
                }

                printf("Drenado de agua terminado.\n");
                printf("Ciclo de lavado terminado.\n");
                idle();
            }
        }

        void dry(int ciclo) {
            if (ciclo == 1) {
                printf("Comenzando a secar la ropa.\n");
                printf("Secando ropa..\n");

                contador = 0;

                for (int i = 0; i < 5; ++i) {
                    printf("%d\n", contador + 1);
                    contador++;
                    Sleep(1000);
                }

                printf("Secado terminado.\n");
                idle();
            }
            if (ciclo == 2) {
                printf("Comenzando a secar la ropa.\n");
                printf("Secando ropa..\n");

                contador = 0;

                for (int i = 0; i < 3; ++i) {
                    printf("%d\n", contador + 1);
                    contador++;
                    Sleep(1000);
                }

                printf("Secado terminado.\n");
                idle();
            }
        }
};

int main() {
    Lavadora lavadora;

    printf("Iniciando ciclo de lavadora.\n");
    lavadora.idle();

    return 0;
}

