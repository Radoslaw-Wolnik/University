#include <stdio.h>
#include <stdlib.h>


main() {
	int i;
	double xp, xk, del;
	
	FILE *p;
	
	scanf("%lf",&xp);
	scanf("%lf",&xk);
	scanf("%lf",&del);
	
	p=fopen("wynik.txt", "w");
	
	for(xp;xp<=xk;xp=xp+del){
		
		fprintf(p, "x= %f    x^2= %f    x^3= %f\n", xp, xp*xp, xp*xp*xp);
		
	}
	
	
	fclose (p);
	
	
	return 0;
}
