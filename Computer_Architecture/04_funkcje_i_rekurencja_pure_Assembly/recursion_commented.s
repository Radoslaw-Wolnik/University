// wypisanie liczby przekazanej jako argument do programu pomnozonej przez 4
// gcc -m32 a.s -o a_out
// eg ./a_out 20
// out: wynik: 80

/* jako zadanie będziemy mieli wyznaczanie ciągu fibbonacziego - zadanie jest do końca semestru bo jest trudniejsze
 * ciąg fibonacziego rekurencyjnie jest najgorszą wersją liczenia ciągu fibonacziego - max argument tak 30 -40 
 * liczy się szybciutko iteracyjnie
*/ 

.intel_syntax noprefix
.global main
.text
main:
	mov eax, [esp + 8]
	mov eax, [eax + 4]
	push eax

	call atoi
	add esp, 4
	
	push eax
	call f
	add esp, 4
	
	push eax
	mov eax, OFFSET msg
	push eax
	call printf
	add esp, 8
	mov eax, 0
	ret
	
	// f(n) = 1          for n = 1
	// f(n) = f(n-1) + n for n > 1 
	// nasza funkcja liczy recursively sume ciągu arytmetycznego r= 1 a1 =1
	// f(n) = sum(i=1->n)i = [n*(n+1)] /2 
	f:
		mov eax, [esp + 4]
		cmp eax, 1
		jne skok
		mov eax, 1 // ale z drugiej strony w eax już było 1 więc w sumie nie potrezbujemy tego
		ret 
		
	// it works but idk how - but he told us that we get stuck on how it works - what is on stack - insted of implementing the recursion
	// we get stuck on thinking what is on stack
	// Im indeed stuck
	// 
	
	skok: 
		dec eax // zmniejszamy eax o  1 : n-1
		push eax // wrzucamy na stos
		call f // wywołujemy funkcje f
		add esp, 4 // dodajemy do stosu 4 - czyścimy stos
		add eax, [esp + 4] // dodajemy do eax - wyniku wykonania funkcji f - poprzednią liczbę - tą co mieliśmy na początku - która aparently jest na stosie + 4
		ret // wracamy - mby na stosie pierwsze od dołu jest to gdzie ma wrócić nasza funkcja a potem poprzedni jest argument funkcji i guess
		// zgadzałoby się
		
	// dziel i żądź - software engeneering holy rule wuuu 


.data
	msg:
	.asciz "Wynik %i\n"
