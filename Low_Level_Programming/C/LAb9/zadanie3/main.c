#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void odwrot(int macierz, int n) {
	int emem;
	
	
}



int main() {
	int macierz [20][20], n, i, j;
	char linia[40], em;
	scanf("%d",&n);
	for (i = 0; i < n; i++){
		for (j = 0; j < n; j ++)
			scanf ("%d",&macierz[i][j]);
		printf("-----------\n");
	}
	
	printf("macierz\n");
	for (i = 0; i < n; i++){
		for (j = 0; j < n; j ++)
			printf ("%d  ",macierz[i][j]);
		printf("\n");
	}
	
	odwrot(macierz,n);
	
	
//	gets( linia ); jakby super by bylo gdyby to bylo wczytywane w jednej liniiiii
//	puts(linia);
	
	return 0;
}
