#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

main () {
//	string lancuch;
	char napis[20], bez[20];
	int i, il=0;
		
	printf("Napisz mi cos\n");
	gets(napis);
//	puts(napis);
	printf("napisales/as: %s\n",napis);
	
	for(i=0; i<=20 ;i++){
		if (napis[i]!=' ')
			bez[i-il]=napis[i];
		else 
		il++;}
	
	printf("bez spacji to: %s\n",bez);
	
	system("pause");
	return 0;
}
