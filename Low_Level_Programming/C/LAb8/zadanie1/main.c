#include <stdio.h>
#include <stdlib.h>

void wyznacznik (double a1, double a2, double b1, double b2, double c1, double c2, double *x, double *y) {
	//  | a1 b1 | = c1
	//  | a2 b2 | = c2
	
	double wg, wx, wy;
	
	wg = a1*b2 - a2*b1;
	wy = a1*c2 - a2*c1;
	wx = c1*b2 - c2*b1;
	
	 
	*x = wx/wg;
	*y = wy/wg;
}


int main() {
	int i;
	double a1, a2, b1, b2, c1, c2, x, y;
	
	printf ("Wyznaczanie wartosci niewiadomych wzorami cramena ax+by=c\n");
	printf ("a1 = ");
	scanf ("%lf",&a1);
	printf ("b1 = ");
	scanf ("%lf",&b1);
	printf ("c1 = ");
	scanf ("%lf",&c1);
	printf ("a2 = ");
	scanf ("%lf",&a2);
	printf ("b2 = ");
	scanf ("%lf",&b2);
	printf ("c2 = ");
	scanf ("%lf",&c2);
	
	wyznacznik(a1, a2, b1, b2, c1, c2, &x, &y);
	
	printf("x = %f i y = %f\n", x, y);
	
	system("PAUSE");
	return 0;
}




