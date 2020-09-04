/*
Mónica Lara Pineda - A01655306
Aldo Fernando Ortiz Mejía - A01654725
Programación Avanzada - TC2025
Rafael Lozano Espinosa
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



