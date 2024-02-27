#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#define maxtab 10

int main() {
	int a [maxtab], b[maxtab], j, i, x, suma;
	for(i=0;i<=10;i++){
		a[i]=10+i;
		b[i]=0;
	}
	
	srand(time(NULL));
//	ogólny wyraz x= rand()%(b+1) losuje liczby od 0 do b
//	ogólny wyraz x= rand()%(b-a+1) +a losuje liczby od a do b
	for(j=1;j<=1000;j++){
	
		x=rand()%(maxtab+1) + 10;
		printf("%d   %d\n",j,x);
		
		for(i=0;i<=10;i++){
		if (x==a[i])
			b[i]++;
		}
		
	}
	
	for(i=0;i<=10;i++){
	printf("liczba %d wystapila %d razy\n",a[i],b[i]);
	}
	
//  sprawdzenie 
	suma=0;
	for(i=0;i<=10;i++){
		suma=suma+b[i];
	}
	printf("%d\n",suma);
	
	system("pause");
	return 0;
}



//w trzech linijkach to co powy¿ej
//for(i=0;1<1000;i++){
//    x=rand()%11 + 10;
//	  tab[x-10]++;
//}
