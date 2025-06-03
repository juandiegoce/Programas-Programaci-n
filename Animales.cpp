#include <conio.h>
#include <stdio.h>
#include <string.h>
//JUAN DIEGO CASTRO ESCOBAR 37A 
class Animal { //Se declara clase principal
    public:
        char animal[50], color[50];
        int ojos, colas, patas;
        
        void ImprimirDatos() { //características comunes de animales
            printf("El %s es de color %s\n", animal, color);
            printf("El %s tiene %d ojos\n", animal, ojos);
            printf("El %s tiene %d cola\n", animal, colas);
            printf("El %s tiene %d patas\n", animal, patas);
        }
};

class Mamifero : public Animal { //se añade clase Mamifero como subclase de animal
    public: 
        void Crianza() {
            printf("El %s nace de su madre\n", animal);
        }
        
        void AlimentacionCrias() {
            printf("El %s alimenta a sus crias con leche materna\n", animal);
        }
        
        void Pelaje() {
            printf("El %s tiene pelaje\n", animal);
        }
        
        void ImprimirMetodosEspecificos() {
            Crianza();
            AlimentacionCrias();
            Pelaje();
        }
};

class Oviparo : public Animal { //se añade clase Oviparo como subclase de animal
    public: 
        void Crianza() {
            printf("El %s nace de un huevo\n", animal);
        }
        
        void AlimentacionCrias() {
            printf("El %s se alimenta por su cuenta al nacer\n", animal);
        }
        
        void Pelaje() {
            printf("El %s no tiene pelaje\n", animal);
        }
        
        void ImprimirMetodosEspecificos() {
            Crianza();
            AlimentacionCrias();
            Pelaje();
        }
};

int main() {
    Mamifero gato;
    Oviparo gallina;

    // Atributos del gato
    strcpy(gato.animal, "gato");
    strcpy(gato.color, "gris atigrado");
    gato.ojos = 2;
    gato.colas = 1;
    gato.patas = 4;
    gato.ImprimirDatos();
    gato.ImprimirMetodosEspecificos();
    
    // Atributos de la gallina
    strcpy(gallina.animal, "gallina");
    strcpy(gallina.color, "blanco con manchas cafés");
    gallina.ojos = 2;
    gallina.colas = 1;
    gallina.patas = 2;
    gallina.ImprimirDatos();
    gallina.ImprimirMetodosEspecificos();
    
    getch();
    return 0;
}
