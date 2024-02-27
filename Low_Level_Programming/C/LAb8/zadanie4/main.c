#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int max (int tab[100], int n){
	int result, i;
	
	for(i=0; i<n; i++){
		if(i==0 || result < tab[i])
			result = tab[i];
	}
	
	return result;
}

int main() {
	int tab[100], N, i;
	srand(time(NULL));
	
	printf ("ile elementow? (max 100) \n");
	scanf("%d",&N);
	
	for (i = 0; i < N; i++){
		tab[i] = rand;
	}
	
	printf("%d\n",max(tab, N));
	
	return 0;
}
