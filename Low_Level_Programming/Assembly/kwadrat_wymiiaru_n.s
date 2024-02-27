.data
msg: .asciiz	"Program wypisuje kwadrat wymiaru N x N:\n"
msg2: .asciiz	"Podaj N: "
gwiazdka: .asciiz "* "
next_line_str: .asciiz "\n"
out: .asciiz	"koniec.\n"
						
.text
main:	
	# wypisuje msg
	la $a0, msg
	li $v0, 4  
	syscall

	# wypisuje msg2
	la $a0, msg2
	li $v0, 4 
	syscall
	
	# pobiera liczbe N
	li $v0, 5
	syscall

	blt $v0, 0, main
	
	# przypisuje t2 = N
	move $t2, $v0
	
	# pod t0 przypisuje 0
	li $t0, 0
	
	# przechodzi do pętli
	j loop_zew


loop_zew:
	# porównuje t0 < N
	beq $t0, $t2, exit

	# pod t1 przypisuje 0
	li $t1, 0
	
	# dodaje 1 do t0
	addi $t0, 1

	# wywołuje petle wewnatrz
	j loop_wew

loop_wew:
	# porównuje t1 < N
	beq $t1, $t2, next_line


	# gwiazdka 
	la $a0, gwiazdka
	li $v0, 4
	syscall
	
	# dodaje 1 do t1
	addi $t1, 1

	# wywołuje ponownie pętle
	j loop_wew


next_line:
	# next line 
	la $a0, next_line_str
	li $v0, 4  
	syscall

	# wywołuje ponownie pętle
	j loop_zew

exit:
	# wypisuje out
	la $a0, out	
	li $v0, 4  
	syscall

	# koniec programu
	li $v0, 10
   	syscall
