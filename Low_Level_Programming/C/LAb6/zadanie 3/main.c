#include <stdio.h>
#include <stdlib.h>
#include <time.h>

main() {
	int i, n;
	double a, x;	
	FILE *pk;
	srand(time(NULL));
	
	scanf("%lf",&a);
	scanf("%d",&n);
	
	pk=fopen("dane.txt", "w");
	
	for(i=0; i<=n; i++){
		
		x= (rand() / (float)RAND_MAX) * (2*a) - a;
		fprintf(pk, "%d   %f\n",i ,x);
	}
	
	fclose (pk);
	
//	system("pause");
	return 0;
}
