/*
Mónica Lara Pineda - A01655306
Aldo Fernando Ortiz Mejía - A01654725
Programación Avanzada - TC2025
Rafael Lozano Espinosa
*/

#include <stdio.h>

int residuo(int* a, int* b) {
    for(int i=0; i<*a; i++) {
        if (*a < *b) {
            return *a;
        }else {
           *a = *a - *b;
        }    
    }
}

int main() {
    int a = 10;
    int b = 3;

    printf("El residuo es: %d", residuo(&a, &b));

    return 0;
}