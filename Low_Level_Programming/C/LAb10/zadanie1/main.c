#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// wejscowka = 1


int fun (char lancuch[11]){
	int result = 0, i, j = 0, koniec;
	
	// sprawdza gdzie jest koniec tablicy
	for(i = 0; i < 11; i++){
	if(lancuch[i] == 10)  // wartosc 10 to koniec tablicy  1234
		koniec = i;
}
//	printf("koniec = %d\n",koniec);
	
	for(i = koniec - 1; i >= 0; i--){
		if(i == koniec - 1)
			result = lancuch[i] - '0';
		if(i < koniec - 1)
			result += (lancuch[i] - '0')* pow(10,j); 
//		printf("%d %d \n",i,result);
		j++;
	}
	
	return result;
}

int main() {
	char napis[11];
	int liczba;
	printf("xd napisz liczbe o dlugosci <= 10 znakow\n");
//	scanf("%s",&napis);  tez powinno byc okay
	fgets(napis, 11, stdin);
	
	liczba = fun(napis);
	
	printf ("twa liczba to %d\n",liczba);
	
	return 0;
}
