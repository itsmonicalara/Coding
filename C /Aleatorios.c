#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>

int main(){
    srand(time(NULL));
    int maquina = rand() % 100 + 1;
    int optimo = (int)log2(100) + 1; 
    printf("El número aleatorio fue %d y el optimo es %d\n", maquina, optimo);
    int intentos = 0;
    //Diferente a lo que puede generar la maquina
    int propuesto = 0;
    while(propuesto != maquina){
        printf("Dame un número entre 1 y 100\n");
        scanf("%d", &propuesto);
        intentos++;
        if(propuesto == maquina){
            printf("Le atinaste en %d oportunidades\n", intentos);
            if(intentos > optimo){
                printf("Tu desempeño puede ser mejo\n");
            }
        }
        else if(propuesto > maquina){
            printf("Tu número esta muy grande\n");
        }
        else{
            printf("Tu número esta muy pequeño\n");
        }
    }
    return 0;
}