/* Programa para leer un palindrome. El número se tiene que leer de igual manera de izquierda a derecha y viceversa. 
Siempre va a haber dos casos: número par e impar de dígitos. El número puede ser ya un palindrome pero pide el sig. 
palindrome más pequeño. 
Casos impares: Se refleja la mitad izquierda de los números y en caso de que el número resultante sea menor al original,
se le agrega una unidad a el dígito de en medio. Por ej. 456 -> 454. Al ser menor se aumenta una unidad al 5 y resulta
464. 
Otro ej. 765 -> 767.
Casos pares: Se refleja de igual forma la mitad izquierda de los números y en caso de que el número resultante sea menor 
al original, se le agrega una unidad a los dos dígitos de en medio. Por ej. 1024 -> 1001.  Al ser menor se aumenta una 
unidad a los 2 ceros y resulta 1111.
Otro ej. 2410 -> 2442. 
En caso de que los digitos de en medio sean 9, se hace un redondeo del número y se hace otra vez el proceso.
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int strCount;

void printNum(char *str){
    int i;
    printf("1%s1\n", str+1);
}

void pairNum(char *str, int half, int index){
    int i;

    for(i = index; i >= 0; i--)
	    str[strCount-i] = str[i];

    printf("%s\n", str);
}

void addDigit(char *str, int half){
    int i;

    for (i = half; i >= 0; i--){
        if (str[i] == '9'){
		    str[i] = str[strCount - i] = '0'; 
        }
	    else{
            str[i]++;
            break;
        }
    }
    
    if (i == -1 && str[i+1] == '0'){
        printNum(str);
        return;
    }

    pairNum(str, half, i);
}

void mirrorNum(char *str){
    int i;
    int half = strCount/2;
    int sign = 0;

    for(i = half; i >= 0; i--){
        if(str[i] > str[strCount-i]){
            sign = 1;
            break;
        }
        else if(str[i] < str[strCount-i]) 
        	break;
    }
    
    if(sign){
    	pairNum(str, half, i);
    } 
    else 
    	addDigit(str, half);
}

int main(int argc, char const *argv[]){
/* k puede tener hasta 1,000,000 digitos, los cuales es imposible meterlos en un int (int no toma más de 10 digitos). 
Se toma el input en char y se guardan en un array */
    int t;
    char arrayK[1000005];

    scanf("%d", &t);
    for(int i = 1; i <= t; i++){
    	scanf("%s", arrayK);
        strCount = strlen(arrayK) - 1;
        mirrorNum(arrayK);
    }
    return 0;
}



