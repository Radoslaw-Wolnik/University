#include <stdio.h>
// gcc -masm=intel programm.c -o out_name
// ./out_name
int main(int argc, char **argv)
{
	int x = 0x39d;
    // zapis szesnastkowy jest wygodny bo zamienia 4 bity na 1 liczbe
	// int ma 8 cyfr szesnastkowych
	int y;
	
	// kod w asemblerze - sprawdzamy ile jest 1 w liczbie binarnej
	// przesuwamy o 1 bit eax
	// sprawdzamy czy dalej cos jest w eax - czy 0
	// idziemy dalej 
	asm (
        "mov eax, %1;"
        // "mov ebx, 0;" // zerujemy wynik -- kompilator nigdy nie bedzie tak robić bo zuzywa 4bajty na 0
        "xor ebx, ebx;" // zamiast tego xor tego samego z tym samym - 0
        //"mov ecx, 32;" // 32 jako counter - integer size
        
        "petla:"
			"shl eax;" // przechodzimy 1 bit dalej; w fladze c mamy informacje czy byla tam 1 czy nie
			"jnc przeskocz;" // jesli flaga jnc jest zgaszona to przeskocz do skok, jesli jest zapalona to nie 
			// "add ebx, 1;" // dodaj 1 do ebx jesli nie przeskocz
			"inc ebx;" // increment ebx by 1
			"przeskocz:"
				//"dec ecx;" // decrement ecx by 1
				// ale zamiast tego mozemy sprawdzic czy w eax dalej cos jest - porownac do 0
				//"cmp eax, 0;" // po przesunieciu o bit sprawdz czy eax to 0 
				"and eax, eax" // ale zamiast tego lepiej jest zrobić operację eax AND eax - zamiast porownania do 0 
				"jnz petla;" // flaga porownania ecx do 32
				
		
		"mov %0, ebx;"
        
        : "=r" (y) // ouput referenced by %0
        : "r" (x) //  input referenced by %1
        : "eax", "ebx", "ecx" // registers that we will use
    );
    // jesli jest jakis blad w assemblerze to uwaza calosc tego co jest w asm("....") jako jedna linijke - tutaj line 11
	// skok w assemblerze nie moze byc wykonany o wiecej niz 127 bajtow do przodu lub 127 bajtow do tylu
	printf("x = %i, hex(x) = %x, y = %i\n", x, x, y);
	return 0;
}

