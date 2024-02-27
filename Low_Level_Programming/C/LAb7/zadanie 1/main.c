#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define float wejscowka = 0.8;
double pi = 3.1415926535;
// funkcja przedzialy jest nie dokoñczona

void rozklad_normalny(FILE *fp, int ilosc){
	int i;
	double number;
	srand(time(NULL));
	
	fp = fopen ("rozklad_normalny.txt","w");
	if (fp != NULL){
		for(i=0;i<ilosc;i++){
		number = ((rand() + 1.0) / (RAND_MAX + 0.0)) * (1 - 0) + 0;
		fprintf(fp,"%lf\n",number);	
		}
		fclose(fp);
	}
}

/*
void rozklad_nienormalny(FILE *fp; FILE *fp2;){
	int i, j, line;
	double res1, res2, liczba1, libcza2;
	
	if ((fp = fopen ("dane.txt","r")) != NULL && fp2 = fopen ("dane2.txt","w")) != NULL) {
	
	for(i = 0; i < 100; i++){
		line = rand()%101;
		//losuje liniê, pobiera liczbê1 z tej lini, natênie losuje drug¹ liniê i pobiera z niej liczbê2
		//podstawia liczbê1 i licbzê2 do wzoru i generuje losowe - rozk³adem gaussa res1 i res2
		//zapisuje res1 i res2 do pliku
		
		
		}
		
	fclose(fp);
	fclose(fp2);
	}	
}
*/

void rozklad_nienormalny(FILE *fp, int ilosc){
	int i, j, k;
	double number[2], res1, res2;
	srand(time(NULL));
	
	fp = fopen ("rozklad_gaussa.txt","w");
	if (fp != NULL){
		
		if(ilosc%2 == 0)
			k = ilosc/2;
		if(ilosc%2 != 0)
			k = ilosc/2 + 1;

		for(i = 0 ; i < k; i++){
			
			for(j = 0; j < 2; j++)
				number[j] = ((rand() + 1.0) / (RAND_MAX + 0.0)) * (1 - 0) + 0;
			
			res1 = (cos(2*pi*number[1])) * (sqrt(-2*log(number[0])));
			res2 = (sin(2*pi*number[1])) * (sqrt(-2*log(number[0])));
			
			fprintf(fp,"%lf\n%lf\n", res1, res2);
			
			/*
			if (k%2 != 0 && k-1 == i)
				fprintf(fp,"%lf\n%lf\n", res1);
			else
				fprintf(fp,"%lf\n%lf\n", res1, res2);
				nvm nie dziala :(*/
				
		}
		fclose(fp);
	}
}

double srednia_arytmetyczna (FILE *fp, int ilosc){
	int i;
	double result = 0.0, number;	
	fp = fopen ("rozklad_gaussa.txt","r");
	if (fp != NULL){
		for(i = 0; i < ilosc; i++){
			fscanf(fp,"%lf",&number);
			result += number;
		}
	fclose(fp);
	}
	return result/(i+1);
}

double odchylenie (FILE *fp, double srednia, int ilosc){
	int i, znak;
	double result, suma=0, number;	
	fp = fopen ("rozklad_gaussa.txt","r");
	if (fp != NULL){
		for(i = 0; i < ilosc; i++){
			fscanf(fp,"%lf",&number);
			number = number*number;
			suma += number;
		}
		
		fclose(fp);
	}
	if (suma<0)
		znak = -1;
	if (suma>0)
		znak = 1;
	
	result = znak * sqrt( fabs( (1.0/(i)) * suma) );
	return result;	
}

void przedzialy (FILE *fp, double srednia, double odchyl, int ilosc){
	int i, p1, p2, p3;
	FILE *result;
	// p1  < srednia - 1*odchylenie; srednia + 1*odchylenie >
	// p2  < srednia - 2*odchylenie; srednia + 2*odchylenie >
	// p3  < srednia - 3*odchylenie; srednia + 3*odchylenie >
	
	fp = fopen("rozklad_gaussa.txt","r");
	if (fp != NULL){
		for(i = 0; i < ilosc; i++){
			fscanf(fp,"%lf",&number);
			
			// sprawdza do którego zakresu nale¿y number i nastêpnie iteruje zmieen¹ odpowiadaj¹c¹ danemu zakresowi
			
			}
			
		fclose(fp);
	}
	
}

int main() {
	int i, ilosc;
	double srednia_ar, odchyl_st;
	FILE *norm;
	FILE *gauss;
	FILE *resu;
	
	printf("ile liczb losowac?\n");
	scanf("%d", &ilosc);
	
	rozklad_normalny (norm, ilosc); //tworzy plik tekstowy o rozkladzie normalnym
	rozklad_nienormalny (gauss, ilosc); //tworzy plik tekstowy o rozkladzie gaussa
	srednia_ar = srednia_arytmetyczna(gauss, ilosc); //oblicza sredni¹ arytmetyczn¹ pliku o rozkladzie gaussa
	odchyl_st = odchylenie(gauss, srednia_ar, ilosc); //oblicza odchylenie standardowe pliku o rozkladzie gaussa
	
	printf("%f\n%f\n",srednia_ar, odchyl_st);
	
	przedzialy(gauss, srednia_ar, odchyl_st, ilosc); //oblicza ile liczb miesci sie w przedzialach & zapisuje do pliku raport.txt
	
	return 0;
}



