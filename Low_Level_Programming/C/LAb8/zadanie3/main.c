#include <stdio.h>
#include <stdlib.h>

void wypisywanie (double xp, double xk, double delx){
	
	for(xp; xp <= xk; xp+=delx)
		printf("%f\n",xp);
	
}


int main() {
	double xp, xk, delx;
	
	scanf("%lf",&xp);
	scanf("%lf",&xk);
	scanf("%lf",&delx);
	
	wypisywanie(xp,xk,delx);
	
	system("PAUSE");
	return 0;
}
