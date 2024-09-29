.intel_syntax noprefix
.global main
.text
main:
	mov eax, [esp + 8]
	mov eax, [eax + 4]
	push eax

	call atoi
	add esp, 4
	
	add eax, eax
	push eax
	mov eax, OFFSET msg
	push eax
	call printf
	
	add esp, 8
	mov eax, 0
	ret


.data
	msg:
	.asciz "Wynik %i\n"

