// wypisanie liczby przekazanej jako argument do programu pomnozonej przez 2
// eg a_out 2024

// IA - 32 STACK RTL 
/* int main(int ARGC, char **ARGV)
 * [ ARGV ] int - wskażnik na tablicę z danymi
 * [ ARGC ] int - wskaźnik na tablicę z danymi też - ale tymi podanymi w trakcie wywołania programu chyba - eg ./a_out 2024 to będzie w tej tablicy 2024
 * [adres przodu ] - początek programu - main - gdzie jest 
 * [ ... ]  - ESP - chyba dalszy ciąg  - program
 * [ ... ]
 * [ ... ] 
*/

// jest jedna z teorii dlaczego rzymianie polegli w swoim systemie niepotrzebnie skomplikowali cyferki
// How ofted do u think about roman empire

// esp + 4 to będzie argC
// esp + 8 to będzie argV - plus 8 bitów chyba - pierwszy argument to nazwa programu drugi to liczba przekazana

/* historia C - zxiom Tomson który napisał linuxa stwierdził że pisanie systemu operacyjnego w Asembly to koszmar więc napisał C
 * no i C chwyciło ale to był oryginalnie język do pisania systemów operacyjnych 
 * i się przyjeło i wszyscy zaczęli używać C i zaczęli wszystko w tym pisać ale wymyslony byłoo pisania OS
*/ i wszystkie języki maja interfejs do C żeby mieć dostęp do sprzętu 

/* int atoi(return *c)
 * pracuje dopóki się uda
 * przekształca łańcuch znaków na liczbę ale jest chujowe i nie należy jej używać 
 * - albo używać na szybko oalbo kiedy wiemy że string jest dobrze sformatowany zawsze
*/


.intel_syntax noprefix
.global main
.text
main:
	mov eax, [esp + 8] // pierwsza referencja wskazuje na początek tablicy ARGV
	mov eax, [eax, + 4] // druga referencja wskazuje na drugi argument w tablicy argV - pierwszy to nazwa programu zawsze
	push eax // push na stos eax

	call atoi // wywołujemy funkcję atoi 
	add esp, 4 // zdejmujemy z stosu i w tym momencie w eax mamy już liczbę która była przekazana do programu - 2024 eg.
	
	add eax, eax
	push eax
	mov eax, OFFSET msg
	push eax
	call printf // printf potrafi wszystko na łańcuch znaków przekształcić i jeszcze jest to formatowanie 
	add esp, 8
	mov eax, 0
	ret // to jest return main


.data
msg:
.asciz "Wynik %i\n"

/* geany file_name.c &
*  gcc file_name.c -o out_file_name
*  gcc -masm=intel -save-temps file_name.c
* touch a.s
* gcc -n32 a.s -o name_out
*/
