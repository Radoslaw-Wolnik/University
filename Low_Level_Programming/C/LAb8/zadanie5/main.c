#include <stdio.h>
#include <stdlib.h>


void fun (FILE *fp){
	//otorz plik tekstowy, przepisz go zamieniajac male litery na duze
}

int main() {
	char lancuch[255], a;
	int i;
	FILE *fp;
	
	//obowiazuje dziesietny system ascii
	a = 97;
	
	printf("zadanie 5\n");
	printf("%c",a);
	
	fp = fopen("dane.txt", "w");
	if (fp != NULL){
		// tu wpisz do pliku tekstowego od uzytkownika
	}
	
	fun(fp);
	
	system("PAUSE");
	return 0;
}
