# include <stdio.h>
int main() {
    char s[] = "Ala ma kota";
    printf("poczatkowy string: %s \n", s);
    // wstwka w assembly
    // chyba najpierw znajdujey koniec i wpisujemy go do rcx
    // potm idziemy z gory na dol i z dolu do gory i zamieniamy
    asm (
        "mov rbx, %0;"
        "mov rcx, rbx;"
        "petla:"
			"mov ah, [rcx];"
			"cmp ah, 0;"
			"je skok;" // /0 - koniec string jest jako 0
			"inc rcx;" // przechodzimy dalej
			"jmp petla;"
		"skok:"
			"dec rcx;"
		"petla2:"
			"cmp rcx, rbx;"
			"jbe koniec;"
			"mov al, [rcx];" // zamieniamy
			"mov ah, [rbx];"
			"mov [rcx], ah;"
			"mov [rbx], al;"
			"inc rbx;" // zwiekszamy
			"dec rcx;" // zmniejszamy
			"jmp petla2;"
		"koniec:"
        : 
        : "r" (s) 
        : "rax", "rbx", "rcx"
    );
    // : wyjscie - gdzie zapisac wyjscie naszej wstawki
    // : wejscie do naszej wstawki - co potrzebujemy z programu; w tej linijce piszemy co czytamy, "r" - register - zostanie zapisane do jakiegos rejestru, "m" - memory
    // : w ostatniej linijce lista rejestrow jakich uzywamy
    printf("koncowy string: %s \n", s);
    return 0;
}
