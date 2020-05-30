#include <stdio.h>
#include <stdlib.h>


// Definici�n de Estructuras
struct partidos
{
 int ganados;
int perdidos;
int empatados;
};
typedef struct partidos P;
struct juegos
{
   char equipo[15];
   int temporadas;
   P part[10];
   float puntos;
};
typedef struct juegos J;

 void llenajuego(J [10],int *);
 void imprime(J[10],int);

int main()
{
    J vj[10];
    int *i=0,opc;
    do
    {
        printf("\n1.Alta Equipo \n2. Imprime todos  \n6.Salir\n");
        scanf("%d",&opc);
        switch(opc)
        {
            case 1:llenajuego(vj,&i);
            break;
            case 2:imprime(vj,i);
            break;
        }
    }while(opc!=6);

    return 0;
}

void llenajuego(J vj[10],int *i)
{
    int j;
    printf("Nombre del equipo ");
    fflush(stdin);
    gets(vj[*i].equipo);
    printf("Cuantos temporadas  se jugaron ");
    scanf("%d",&vj[*i].temporadas);
    for (j=0;j<vj[*i].temporadas;j++)
    {
        printf ("\nJuegos ganados en temporada %d  ",j);
        scanf("%d",&vj[*i].part[j].ganados);
        printf("\n Juegos perdidos en temporada %d  ",j);
        scanf("%d",&vj[*i].part[j].perdidos);
        printf("\nJuegos empatados en temporada %d ",j);
        scanf("%d",&vj[*i].part[j].empatados);
    }
    *i=*i+1;
}

void imprime(J vj[10],int i)
{
    int j,k;
    for (k=0;k<i;k++)
    {
        printf("\n          Nombre del equipo  %s ",vj[k].equipo);
        printf("\n\n");
        printf("\n  Temporadas %d  \n ",vj[k].temporadas);

        for (j=0;j<vj[k].temporadas;j++)
        {
           printf ("\nJuegos ganados %d  Perdidos    %d   Empatados %d  \n ",vj[k].part[j].ganados,vj[k].part[j].perdidos,vj[k].part[j].empatados);

         }
    }

}