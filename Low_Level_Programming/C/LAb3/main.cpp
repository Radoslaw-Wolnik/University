#include <iostream>
#include<math.h>
#include<stdio.h>

int main() {
	
	double numb, sth, zakres, prev, next, yh;
	int i;
	
	printf("Witaj\npodaj liczbe do pierwiastka kwadratowego ");
	scanf("%lf",&numb);
	printf("podaj zakres bledu ");
	scanf("%lf",&zakres);
	
	prev=numb/2;
	next=1;
	for(i=1;(next-next)<zakres;i++){
		
		next=1.0/2*(prev+numb/prev);
		printf("%f\n",next);
		prev=next;
	}
	
	printf("Wartosc to %f",next);
	
	system("pause");
	return 0;
}
