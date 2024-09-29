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
	asm (
        "mov eax, %1;"
        // "mov ecx, 0;" // zerujemy counter -- kompilator nigdy nie bedzie tak robić bo zuzywa 4bajty na 0
        "xor ecx, ecx;" // zamiast tego xor tego samego z tym samym - 0
        // "mov ebx, 0;" // zerujemy wynik
        "xor ebx, ebx;"
        
        "petla:"
			"shl eax;" // przechodzimy 1 bit dalej; w fladze c mamy informacje czy byla tam 1 czy nie
			"jnc przeskocz;" // jesli flaga jnc jest zgaszona to przeskocz do skok, jesli jest zapalona to nie 
			// "add ebx, 1;" // dodaj 1 do ebx jesli nie przeskocz
			"inc ebx;" // increment ebx by 1
			"przeskocz:"
				// "add ecx, 1;" // dodaj 1 do counter
				"inc ecx;" // increment ecx by 1
				"cmp ecx, 32;" // porownaj ecx do 32
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

