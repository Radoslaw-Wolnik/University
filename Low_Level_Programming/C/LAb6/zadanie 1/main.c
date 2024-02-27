#include <stdio.h>
#include <stdlib.h>


	struct point {
		double x, y;
	};
	
	struct circle {
		double r;
		struct point punkt;
	};
	
	struct square {
		struct point d0, d1;
	};
	
	
	double odleglosc (double x1, double x2, double y1, double y2) {
	double wynik;
	wynik = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
	return wynik;
}


main() {
	int i=1,g;
	struct point punkt1, punkt2;
	struct circle okrag;
	struct square kwadrat;
	double wynik, em;
	
/*	okrag.punkt.x = 10;
	okrag.punkt.y = 6;
	okrag.r = 3;
	
	printf("%f\n",okrag.r);
	printf("%f\n",okrag.punkt.x);
	printf("%f\n",okrag.punkt.y); */
	
	
	while(i==1){
		
		printf("oblicz odleglosc miedzy punktami - 1\n");
		printf("oblicz pole kola - 2\n");
		printf("oblicz pole kwadratu - 3\n");
		scanf("%d",&g);
		
		if(g==1){
		printf("podaj pierewszy punkt\n x=");
		scanf("%lf",&punkt1.x);	
		printf(" y=");
		scanf("%lf",&punkt1.y);
		printf("podaj drugi punkt\n x=");
		scanf("%lf",&punkt2.x);
		printf(" y=");
		scanf("%lf",&punkt2.y);
		wynik = sqrt ((punkt1.x-punkt2.x)*(punkt1.x-punkt2.x) + (punkt1.y-punkt2.y)*(punkt1.y-punkt2.y));
		printf("odleglosc to %f\n",wynik);
			
		}
		
		if(g==2){
			printf("podaj srodek okregu\n x=");
		scanf("%lf",&okrag.punkt.x);	
		printf(" y=");
		scanf("%lf",&okrag.punkt.y);
		printf("podaj promien = ");
		scanf("%lf",&okrag.r);
		wynik = okrag.r*okrag.r*3.1415926535;
		printf("pole to %f\n",wynik);
			
		}
		
		if(g==3){
		printf("podaj poczatek przekontnej kwadratu\n x=");
		scanf("%lf",&kwadrat.d0.x);	
		printf(" y=");
		scanf("%lf",&kwadrat.d0.y);
		printf("podaj koniec przekontnej kwadratu\n x=");
		scanf("%lf",&kwadrat.d1.x);
		printf(" y=");
		scanf("%lf",&kwadrat.d1.y);	
		
		em = sqrt((kwadrat.d0.x-kwadrat.d1.x)*(kwadrat.d0.x-kwadrat.d1.x) + (kwadrat.d0.y-kwadrat.d1.y)*(kwadrat.d0.y-kwadrat.d1.y));
		wynik = em*em/2;
		printf("pole to %f\n",wynik);
			
			
		}
	
	printf("Exit - 0   Again - 1\n");
	scanf("%d",&i);
	printf("\n\n\n\n");
	}
	//wejsciowka 6 = 0.7
	//wejsciuwka 5 = 0.9
	system("pause");
	return 0;
}



