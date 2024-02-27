#include <iostream>
#include <stdio.h>
#include <math.h>

int main() {
	printf("Hey\n");
	
	int a[3], i, t;
	a[0]=0;
	a[1]=0;
	a[2]=0;
	a[3]=0;
	t=1;
	i=0;
	printf("ver a\n");
	for(;t==1;i++){
		
		scanf("%d",&a[i]);
		
		if(i>0 && a[i-1]!=1 && a[i]==1){
			i=0;
			a[i]=1;
			printf("pierwsza\n");}
		
		if(i==3 && a[i]!=1){
			i=0;
			printf("kasuje, i = %d\n",i);		
		}
		if(i==3 && a[i]==1){
			a[0]=1;
			i=1;
			printf("trzecia\n");}
			
		if(a[0]==a[1] && a[1]==a[2] && a[2]==1){
			printf("czwarta\n");
			break;}
				
		
	}
	
	
	printf("yay\n");
	system ("pause");
	return 0;
}
