/*
Mónica Lara Pineda - A01655306
Aldo Fernando Ortiz Mejía - A01654725
Programación Avanzada - TC2025
Rafael Lozano Espinosa
*/

#include <stdio.h>
#include <stdbool.h>
#include <math.h>


int main() {

	int t;
	int m;
	int	n;

	scanf("%d", &t);

	for (int i = 1;i <= t; i ++) {
		scanf("%d %d", &m, &n);

	for	(int num = m; num <= n;num ++){
		if (num <= 1) {
			continue;
		}
			bool esPrimo = true;

			for (int j = 2; j <= sqrt(num); j++) { 
				if (num % j == 0) {
					esPrimo = false;
					break; 

			}
			}

			if (esPrimo == true){
				printf("%d\n", num);
			}
		}
	}
	return 0;

}