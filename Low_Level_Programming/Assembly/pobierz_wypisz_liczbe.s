.data
msg: .asciiz	"\nkoniec\n"	
						
.text
main:		
	li $v0, 5  # pobiera
	syscall

	move $t0, $v0
	li $v0, 1  # wypisuje 
   	move $a0, $t0
    	syscall

	li $v0, 4  # wypisuje 
	la $a0, msg
	syscall

	li $v0, 10 # konczy dzialanie
   	syscall