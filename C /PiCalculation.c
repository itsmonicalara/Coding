//Calculo del valor de pi con una seria
#include <stdio.h>

int main(){
	int n;
	printf("Dame el número de iteraciones\n");
	scanf("%d", &n);

	float res = 0;
	float div = 1;
	int suma = 1;
	for(int i = 0; i < n; i++){
		res += suma*4/div;
		suma *= -1;
		div += 2;
		printf("El resultado es %f\n", res);
	}
	return 0;
}
