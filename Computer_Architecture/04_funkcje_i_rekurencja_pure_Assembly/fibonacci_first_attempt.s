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
	
	f:
		mov eax, [esp + 4]
		cmp eax, 2
		jg skok // jeśli jest wieksze od 2 to zwracamy skok
		// mov eax 1 // w przeciwnym wypadku 
		pop eax // were egting where to return to eax
		push 1
		push eax
		ret 
		
	skok: 
	    mov eax, [esp + 8]
		dec eax
		push eax
		call f
		mov eax, [esp + 4]
		dec eax
		push eax
		call f
		pop eax
		add eax, [esp]
		add esp, 12
		pop ebx
		push eax
		push ebx
		ret
	// jaki będzie problem - zapamietanie tego n-1 i n-2
	// pamięć jest niedobra, rejest też jest nie dobry bo będzimey sobie to nadpisywać
	// więc musimy zapamiętać na stosie ale jeśli zapamiętamy na sytosie to nam się przenumerowuje ilość rzeczy na stosie
	// jeśli zdążymy to na ostatnich zajęciach zobaczymy jak się to robi tak na prawdę 

.data
	msg:
	.asciz "Wynik %i\n"

// 0, 1, 1, 2, 3, 5, 8, 11, 19, ...
// ./fib 1 -> 0 ./fib 2 -> 1 ./fib 4 -> 2 ./fib

f(n) = 1 dla n = {1,2}
f(n) = f(n-1) + f(n-2) dla n > 2
 
// recursion jest stosożerna
// budujemy ciągle stos a potem w warunkach wyjścia zjadmay
// rekurencja jest fajna jak się uczymy ale w rzeczywistości jak nie panujemy nad liczbą przekazaną do rekurencji to tak średnio bo wywala się niskopoziomowo
