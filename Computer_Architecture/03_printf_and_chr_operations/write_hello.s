.intel_syntax noprefix
.global main
.text 
main:
mov eax, OFFSET mesg 
push eax 
call printf
pop eax
mov eax, 0
ret

.data
mesg:
.asciz "Hello World\n"
