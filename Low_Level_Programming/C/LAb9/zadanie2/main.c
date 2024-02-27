#include <stdio.h>
#include <stdlib.h>

double horner (int n, double x, double wsp[20]){
	int i;
	double wynik = 0;
	
	for(i = 0; i < n; i++){
		if (i == 0)
			wynik = wsp[i];
		else
			wynik = wynik * x + wsp[i];
	}
	
	return wynik;
}


int main() {
	int n, i;
	double iks, wynik, wsp[20];
	
	printf("wartosc wielomianu\n");
	printf("podaj ile wyrazow: ");
	scanf("%d",&n);
	
	
	for(i = 0; i < n; i++){
		printf("a%d = ",i);
		scanf("%lf",&wsp[i]);
	}
	
	printf("podaj dla jakiej wartosci: ");
	scanf("%lf",&iks);
	
//	wynik = wartosc (n, iks, wsp);
	wynik = horner (n, iks, wsp);
	
	printf ("wartosc = %f\n",wynik);
	
	
	
	system("PAUSE");
	return 0;
}
