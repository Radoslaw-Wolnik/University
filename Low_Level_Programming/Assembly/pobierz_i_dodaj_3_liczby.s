.data
msg1: .asciiz	"Program dodaje 3 liczby\npodaj liczbe 1:\n"
msg2: .asciiz	"podaj liczbe 2:\n"
msg3: .asciiz	"podaj liczbe 3:\n"
out: .asciiz	"Dodane liczby:\n"	
						
.text
main:	
	# wypisuje 
	la $a0, msg1	
	li $v0, 4  
	syscall

	# pobiera liczbe
	li $v0, 5
	syscall
	
	move $t0, $v0

	# wypisuje 
	la $a0, msg2	
	li $v0, 4  
	syscall

	# pobiera liczbe
	li $v0, 5
	syscall
	
	move $t1, $v0

	# wypisuje 
	la $a0, msg3	
	li $v0, 4  
	syscall

	# pobiera liczbe
	li $v0, 5
	syscall

	add $t0, $v0, $t0
	add $t0, $t0, $t1

	# wypisuje
	li $v0, 4  
	la $a0, out
	syscall

	move $a0, $t0 # a0 = t0
	li $v0, 1
	syscall

	li $v0, 10 # konczy dzialanie
   	syscall