// wypisanie liczby przekazanej jako argument do programu pomnozonej przez 4
// gcc -m32 a.s -o a_out
// eg ./a_out 20
// out: wynik: 80


.intel_syntax noprefix
.global main
.text
main:
	mov eax, [esp + 8]
	mov eax, [eax + 4]
	push eax

	call atoi
	add esp, 4
	
	// add eax, eax // now insted of just adding two eax we will call a function - our function
	
	push eax // dajemy na stos eax
	call f // wywołujemy naszą funkcję
	add esp, 4 // zdejmujemy z stosu
	
	push eax
	mov eax, OFFSET msg
	push eax
	call printf
	add esp, 8
	mov eax, 0
	ret
	
	// funkcja widoczna tylko w ramach tego programu, gdybyśmy dodali do . global to będzie poza ale nikt nie pisze bibliotek w Asembly now 
	f:
		mov eax, [esp + 4] // + 4 żeby przeskoczyć nad adresem powrotu
		add eax, eax
		add eax, eax
		ret 
	// kiedy system woła naszą aplikację to nie woła przez call bo wtedy progrma - process miałby stos i mógłby go zmieniać 
	// więc system nie woła w ten sposób - zasada ograniczonej odpowiedzialności -  
	// opisać różne rodzaje przerwań

.data
	msg:
	.asciz "Wynik %i\n"
