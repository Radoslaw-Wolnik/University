.data
msg1: .asciiz	"Program porownuje dwie liczby\nPodaj liczbe 1:\n"
msg2: .asciiz	"Podaj liczbe 2:\n"
out1: .asciiz	"Liczba 1 jest wieksza od liczby 2\n"
out2: .asciiz	"Liczba 1 jest mniejsza od liczby 2\n"
out3: .asciiz	"Podane liczby sa sobie rowne\n"
						
.text
main:	
# -------------------------- pobiera liczby
	# wypisuje 
	la $a0, msg1	
	li $v0, 4  
	syscall

	# pobiera liczbe 1
	li $v0, 5
	syscall
	move $t0, $v0

	# wypisuje 
	la $a0, msg2	
	li $v0, 4  
	syscall

	# pobiera liczbe 2
	li $v0, 5
	syscall
	
# -------------------------- porownuje
	bgt $t0, $v0, wieksze
	blt $t0, $v0, mniejsze
	beq $t0, $v0, rowne
	

wieksze:
	li $v0, 4  
	la $a0, out1
	syscall
	j exit

mniejsze:
	li $v0, 4  
	la $a0, out2
	syscall
	j exit

rowne:
	li $v0, 4  
	la $a0, out3
	syscall
	j exit

exit:
	li $v0, 10
   	syscall
