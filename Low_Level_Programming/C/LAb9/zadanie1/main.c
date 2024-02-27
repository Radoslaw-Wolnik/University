#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void wierzcholek (double a, double b, double c, double *p, double *q){
	*p = -b/(2*a);
	*q = a * *p * *p + b * *p + c;
}

int main() {
	double a, b, c, p, q;
	
	printf("ax^2 +bx +c\n");
	printf("a = ");
	scanf("%lf",&a);
	printf("b = ");
	scanf("%lf",&b);
	printf("c = ");
	scanf("%lf",&c);
	
	wierzcholek (a,b,c,&p,&q);
	
	printf("wierzcholek funkcji w pkt (%f, %f)\n",p,q);
	
	system("PAUSE");
	return 0;
}

// 0.9
