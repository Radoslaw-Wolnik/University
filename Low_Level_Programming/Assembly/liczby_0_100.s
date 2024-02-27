.data
msg: .asciiz	"Program wypisuje liczby od 0 do 100:\n"
next_line: .asciiz "\n"
out: .asciiz	"koniec.\n"
						
.text
main:	
	# wypisuje msg
	la $a0, msg
	li $v0, 4  
	syscall
	
	# przypisuje t0 = 0
	li $t0, 0
	
	# przechodzi do pętli
	j loop


loop:
	# porównuje t0 < 100
	bgt $t0, 100, exit

	# wypisuje 
   	move $a0, $t0
	li $v0, 1
    	syscall

	# next line 
	la $a0, next_line
	li $v0, 4  
	syscall
	
	# dodaje 1 do t0
	add $t0, $t0, 1

	# wywołuje ponownie pętle
	j loop

exit:
	# wypisuje out
	la $a0, out	
	li $v0, 4  
	syscall

	# koniec programu
	li $v0, 10
   	syscall
