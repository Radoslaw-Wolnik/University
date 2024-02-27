#include <stdio.h>
#include <stdlib.h>


main() {
	int i, em, min, eh;
	
	for(i=0;i<20;i++){
		scanf("%d",&em);
		if (i==0 || em<min){
		min=em;
		eh=i+1;}
	}
	
	printf("---------------------------\nminimalna liczba to %d\n",min);
	printf("zostala wpisana jako %d\n\n\n\n\n",eh);
		
	system ("pause");
	return 0;
}
