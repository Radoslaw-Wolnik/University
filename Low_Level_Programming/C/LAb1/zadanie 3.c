#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main(){
	
	float x,y;
	printf("wpisz x: ");
	scanf("%f",&x);
	if(x>0)
	 y=x*x+exp(2*x);
	else if(x==0)
			y=2;
			
		//wieksze od 0
		
		
	else
		y=sqrt(fabs(2+x));
	
	
	printf("%f",y);
	
	
	return 0;
}
