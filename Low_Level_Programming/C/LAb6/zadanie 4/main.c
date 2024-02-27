#include <stdio.h>
#include <stdlib.h>

main() {
	int i, x;	
	FILE *pk;
	FILE *em;
	FILE *hm;
	
	pk=fopen("dane.txt", "r");
	
	while(fscanf(pk,"%d",&x)==1){
		
		if(x>0){
		em=fopen("dodatnie.txt", "a");
		fprintf(em,"%d\n",x);
		fclose (em);	
		}
		
		if(x<0){
		hm=fopen("ujemne", "a");
		fprintf(hm,"%d\n",x);
		fclose (hm);	
		}
		
		fclose (pk);
	}
	
	
//	system("pause");
	return 0;
}
