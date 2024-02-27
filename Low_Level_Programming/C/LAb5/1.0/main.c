#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#define maxtab 10

main() {
	int a [maxtab] ,j,i,x;
	for(i=0;i<=10;i++){
		a[i]=10+i;
	}
	
	srand(Time(NULL));
//	ogólny wyraz x= rand()%(b+1) losuje liczby od 0 do b
//	ogólny wyraz x= rand()%(b-a+1) +a losuje liczby od a do b
	for(j=1;j<=1000;j++){
		x=rand()%(maxtab+1) + 10;
		printf("%d   %d\n",j,x);
	}
	
	
	
	
	
	system("pause");
	return 0;
}
