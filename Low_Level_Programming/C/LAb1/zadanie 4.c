#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main(){
	float a,b,c, x,y,del,x1,x2;
	
	printf("y=ax^2+bx+c\n");
	printf("a=");
	scanf("%f",&a);
	printf("b=");
	scanf("%f",&b);
	printf("c=");
	scanf("%f",&c);
	printf("x=");
	scanf("%f",&x);
	
	y=a*x*x+b*x+c;
	del=b*b-4*a*c;
	
	if (del==0){
		x1 = -b/2*a;
		x2 = x1;
	}
	if(del>0){
		x1=(-b+sqrt(del))/2*a;
		x2=(-b-sqrt(del))/2*a;
	}
	if(del<0)
	printf("delta ujemna, liczby zespolone\n");
	
	printf("y=%f",y);
	
	if (del>=0)
	printf("x1=%f,x2=%f",x1,x2);
	
	return 0;
	
}
