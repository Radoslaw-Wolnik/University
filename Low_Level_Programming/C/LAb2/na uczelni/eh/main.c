#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

main(){
	int il,n,i,sum,sumpl,ilocz,z,summin;
	float sr,srmin;
	sum=0;
	sumpl=0;
	summin=0;
	ilocz=1;
	z=0;
	printf("ile razy?'\n");
	scanf("%d",&il);
	for(i=1;i<=il;i++){
		printf("liczba: ");
		scanf("%d",&n);
		sum=sum+n;
		printf ("suma wszystkich wynosi %d\n",sum);
		sr=(float)sum/i;
		printf("srednia wynosi %f\n",sr);
		if(n>0){
			sumpl=sumpl+n;
			printf ("suma dodatnich wynosi %d\n",sumpl);
		}
		
		if(n<0){
			z=z+1;
			summin=summin+n;
			srmin=summin/z;
		}
		
		if(n%2==0){
			ilocz=ilocz*n;
			printf("iloczyn dodatnich wynosi %d\n",ilocz);
		}
		
		
	}
	
	return 0;
}
