#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
	int xy;
	float a,b,c, x,y,z;
	b=7.5;
	
	printf("zadanie 1\nWybierz przyklad:");
	scanf("%d",&xy);
	
	if (xy==1){

   		printf("1.a\n");
   		printf("b = %f\n",b);
   		printf("a=(c^2+b^2)^1/2\nPodaj c: ");
    	scanf("%f",&c);
    	a=sqrt(c*c+b*b);
    	printf("a=%f\n",a);
    	system("pause");	
	}
	
	if (xy==2){
		
		printf("1.b\n");
		printf("y=2x^4+bx^3+cx^2+8\n");
		printf("b = %f\n",b);
		printf("podaj c: ");
		scanf("%f",&c);
		printf("podaj x: ");
		scanf("%f",&x);
		
		if (x<0){
			x=fabs(x);
			y=2*pow(x,4)-b*pow(x,3)+c*pow(x,2)+8;	
		}
		else{	
			y=2*pow(x,4)+b*pow(x,3)+c*pow(x,2)+8;	
		}
		
		printf("y wynosi %f\n",y);
		system("pause");
	}
	
	if (xy==3){
		printf("1.c\n");
		printf("y=(1/3+sin(x/2)*(x^3+3))^1/3\n");
		printf("podaj x: ");
		scanf("%f",&x);
		
		if (x<0){
		x=fabs(x);
		y=-pow(((1.0/3+sin(x/2))*(x*x*x+3)),1.0/3);	}
		else{
		y=pow(((1.0/3+sin(x/2))*(x*x*x+3)),1.0/3);}
		printf("y wynosi = %f",y);
		system("pause");
		
	}
	
	if(xy==5){
		printf("tyle zabawy\n");
		scanf("%f",&x);
		z=sqrt(x+2);
		printf("%f",z);		
	}
	
	

    
    return 0;
}

