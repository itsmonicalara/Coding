#include <stdio.h>

void imprime(short a){
    for (int i = 0; i < 16; i++){
       short bit = a & 0x0001;
       printf("el valor %i\n", bit);
       a >>= 1; 
    }
}
//Apuntador a un entero, por eso *
void swap(int* a, int* b){
    int tmp;
    tmp = *a;
    *a = *b;
    *b = tmp;
}

int main(int argc, char ** argv){
    /*short s = -1;
    scanf("%hd", &s);
    imprime(s);
    */
   int x = 20;
   int y = 123;
   //Obtener la dirección de x 
   swap(&x,&y);
   printf("el valor de x es %d y el valor de y es %d\n", x, y);
    return 0;
}