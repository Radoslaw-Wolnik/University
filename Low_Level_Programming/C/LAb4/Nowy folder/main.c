#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int i=0, koniec, g;
	double x, dok, wynik, prev, next, wart, sum, y;
	
	//printf("Wish you luck/n/n/n");
	printf("podaj liczbe x = ");
	scanf("%lf",&x);
	printf("podaj dokladnosc = ");
	scanf("%lf",&dok);	
	printf("podaj po ilu probach chcesz zakonczyc = ");
	scanf("%d",&koniec);	
	
	sum=0;
	next=1;
	prev=0;
	
	while ((i+1)<koniec){
		
		prev=next;
		
		if(i%2==0)
		g=1;
		else
		g=-1;
		
		wart=g*pow(x,(i+1));
		wart=wart/(i+1);
		
		printf("%d     %f     %f\n",i+1,wart,sum);
		
		next=wart;
		i=i+1;	
		sum=sum+wart;
		if(i==0)
			prev=0;
			
		y=(next-prev);
		
		if(fabs(y)<dok)
			break;
		
	}
	
	printf("ln z x = %f\n",sum);
	
	if((i+1)==koniec)
		printf("zatrzymane z powodu ilosci prob\n");
	if((next-prev)<dok)
		printf("zatrzymane ponoiewaz dok\n");
	
	
// 	wejœciówki 1 + 0.7 + 0.8 + 1
	
		
	system("pause");
	return 0;
}
	
