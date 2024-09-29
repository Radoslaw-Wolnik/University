# include <stdio.h>
int main() {
    char s[] = "Ala ma kota";
    printf("poczatkowy string: %s \n", s);
    // wyznaczamy dlugosl str i jednoczesnie zmieniamy male lietery na duze
    // potem odwracamy str
    asm (
        "mov rbx, %0;"
        "mov rcx, rbx;"
        "change_case:"
			"mov ah, [rcx];"
			"cmp ah, 'a';"
			"jl skip;"
			"cmp ah, 'z';"
			"jg skip;"
			"sub ah, 32;"
			"mov [rcx], ah;" // swap small to big letter
			"skip:"
			    "cmp ah, 0;"
			    "je end_str;" // /0 - koniec string jest jako 0
			    "inc rcx;" // przechodzimy dalej
			    "jmp change_case;"
		"end_str:"
			"dec rcx;"
		"reverse_str:"
			"cmp rcx, rbx;"
			"jbe koniec;"
			"mov al, [rcx];"
			"mov ah, [rbx];"
			"mov [rcx], ah;"
			"mov [rbx], al;"
			"inc rbx;"
			"dec rcx;"
			"jmp reverse_str;"
		"koniec:"
        : 
        : "r" (s) 
        : "rax", "rbx", "rcx"
    );
    printf("koncowy string: %s \n", s);
    return 0;
}
