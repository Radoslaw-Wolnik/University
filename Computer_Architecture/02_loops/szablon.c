#include <stdio.h>

int main(int argc, char **argv)
{
	int x = 2024;
    int y;
	
	asm (
        "mov eax, %1;"
        "add eax, eax;"
        "mov %0, eax;"
        : "=r" (y)
        : "r" (x) 
        : "eax", "ebx"
    );
    // "kod w assemblerze"
    // : wyjscie - gdzie zapisac wyjscie naszej wstawki
    // : wejscie do naszej wstawki - co potrzebujemy z programu; w tej linijce piszemy co czytamy, "r" - register - zostanie zapisane do jakiegos rejestru, "m" - memory
    // : w ostatniej linijce lista rejestrow jakich uzywamy

	return 0;
}

