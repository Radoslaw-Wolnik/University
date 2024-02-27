#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double fun (double x, double y){
	double result;
	if (x < y)
		result = 2*x + 2*y;
	if (x == y)
		result = 3;
	if (x > y)
		result = x*x - sin(y);
	
	return result;
}


int main() {
	double licz[7];
	int i;
	
	for(i = 0; i < 6; i++){
	scanf ("%lf",&licz[i]);
	}
	
	licz[7] = 0;
	
	for (licz[4]; licz[4] < licz[5]; licz[4] + licz[2]){
//nwm		licz[7]+=fun();
	}
	
	printf("%f\n", licz[7]);
	
	system("PAUSE");
	return 0;
}
