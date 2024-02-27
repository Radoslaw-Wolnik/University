.data
msg1: .asciiz	"podaj liczbe:\n"
msg2: .asciiz	"powiekszona liczba:\n"	
						
.text
main:	
	# wypisuje 
	la $a0, msg1	
	li $v0, 4  
	syscall

	# pobiera liczbe
	li $v0, 5
	syscall

	add $t0, $v0, 5

	# wypisuje
	li $v0, 4  
	la $a0, msg2
	syscall

	move $a0, $t0 # a0 = t0
	li $v0, 1
	syscall

	li $v0, 10 # konczy dzialanie
   	syscall