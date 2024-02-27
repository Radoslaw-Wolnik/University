#include <stdio.h>
#include <stdlib.h>

main(){
	int t;
	double xp,xk,del,x1,x2,x3,XP;
	printf("zadanie 1\npodaj xp: ");
	scanf("%lf",&xp);
	printf("podaj xk: ");
	scanf("%lf",&xk);
	printf("podaj del: ");
	scanf("%lf",&del);

//	if (xk<xp){
//		t=xk;
//		xk=xp;
//		xp=t;
//	}
	XP=xp;
	for (;xp<=xk;xp=xp+del){
		x1=xp;
		x2=xp*xp;
		x3=xp*xp*xp;
		printf("%f,%f,%f\n",x1,x2,x3);
	}
	if (xp==xk)
		printf("\n\n\n");
		
	xp=XP;
	while(xp<=xk){
		x1=xp;
		x2=xp*xp;
		x3=xp*xp*xp;
		printf("%f,%f,%f\n",x1,x2,x3);
		xp=xp+del;
	}
	
	system("pause");
	return 0;
}
