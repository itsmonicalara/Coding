#include <stdio.h>

void imprime(int*, int);

//Arreglo ascendente
int asc(int a, int b){
	if(a > b){
		return 1;
	}else if(a < b){
		return -1;
	}return 0;
}

int des(int a, int b){
	return asc(b,a);
}

void burbuja(int *arr, int size, int (f(int,int))){
	int swap = 1;
	int comp = size - 1;
	while(swap){
		swap = 0;
		for(int i = 0; i < comp; i ++){
			if(f(arr[i], arr[i+1]) == 1){
				swap = 1;
				int temp = arr[i];
				arr[i] = arr[i+1];
				arr[i+1] = temp;
			}
		}
		comp --;
	}
}

void imprime(int *arr, int size){
	for(int i = 0; i < size; i++)
		printf("%d\t", arr[i]);
	printf("\n");
}

int main(){
	/*int a = 10;
	int b = 20;
	printf("asc de %d, %d es %d \n", a,b, asc(a,b));*/
	int arr[] = {10,-2,6,12,3,-10};
	int size = sizeof(arr)/sizeof(int);
	imprime(arr,size);
	burbuja(arr,size,asc);
	imprime(arr,size);
	return 0;
}