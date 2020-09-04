#include <stdio.h>

int main(int argc, char * argv[]){
	printf("Hola %s, el número de argumentos que pasaste fue de %d\n", argv[0], argc);
	short s = 32766;
	s++;
	printf("El valor %i\n", s);
	return 0;
}