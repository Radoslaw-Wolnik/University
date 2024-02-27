.data
str1: .asciiz	"Hello World!\n"
str2: .asciiz	"Radoslaw Wolnik\n"	
						
.text
main:		
	li $v0, 4			
	la $a0, str1
	syscall
				
	la $a0, str2	
	syscall	

	li $v0, 10	
	syscall				