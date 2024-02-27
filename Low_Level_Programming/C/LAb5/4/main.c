#include <stdio.h>
#include <stdlib.h>


main() {
	int i, dod, a[10];
	
	for(i=0;i<10;i++){
		scanf("%d",&a[i]);
	}
	for(i=0;i<5;i++){
		dod=a[i];
		a[i]=a[10-i];
		printf("%d\n",a[i]);
	}
	
	system("pause");
	return 0;
}
