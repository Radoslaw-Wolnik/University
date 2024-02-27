#include <stdio.h>
#include <stdlib.h>
#include<math.h>


int main() {
	int i;
	double x, max, suma=0, iloczyn=1, srednia, del, a, b;
	i=1;
	
	printf("Podaj kres dolny ");
	scanf("%lf",&a);
	printf("Podaj kres gorny ");
	scanf("%lf",&b);
	printf("Podaj delte ");
	scanf("%lf",&del);

	for(;a<=(b+0.01*del);){
		if(a<-0.01*del)
			x=a*a*a+1/a;
		if(a>(-0.1*del) && a<(0.1*del)) //jeœli a jest wiêksze od -0.01*del i mniejsze od 0.01*del
			x=3*sqrt(2);
		if(a>0.01*del)
			x=pow((sin(sqrt(x))),(1.0/3.0));
		
		if(i==1 || max<x)
			max=x;
		
		suma=suma+x;
//		iloczyn=iloczyn*x;

		
		printf("%f             ",a);
		printf("%f\n",x);
		a=a+del;
		i=i+1;
	}
	
	srednia=suma/i;
	
	printf("A wiec...\nsrednia wynosi %f\nmax wartosc wynosi %f\n",srednia,max);
	system("pause");
	
	return 0;
}
