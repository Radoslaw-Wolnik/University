.data
msg: .asciiz	"Program wypisuje kwadrat wymiaru N x N:\n"
msg2: .asciiz	"Podaj N: "
gwiazdka_msg: .asciiz "* "
spacja_msg: .asciiz "  "
next_line: .asciiz "\n"
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
	# iterator $t0
	# dodaje 1 do t0
	addi $t0, 1

	# next line 
	la $a0, next_line
	li $v0, 4  
	syscall

	# porównuje t0 < N
	bgt $t0, $t2, exit

	# pod t1 przypisuje 1
	li $t1, 1

	# wywołuje petle wewnatrz
	j loop_wew

loop_wew:
	# iterator $t1
	# porównuje t1 < N
	bgt $t1, $t2, loop_zew
	
	# jesli t0 == 0 lub t0 == N
	beq $t0, 1, gwiazdka
	beq $t0, $t2, gwiazdka
	
	beq $t1, 1, gwiazdka
	beq $t1, $t2, gwiazdka

	j spacja
	

gwiazdka:
	# gwiazdka 
	la $a0, gwiazdka_msg
	li $v0, 4
	syscall

	# dodaje 1 do t1
	addi $t1, 1

	# wywołuje ponownie pętle
	j loop_wew

spacja:
	# gwiazdka 
	la $a0, spacja_msg
	li $v0, 4
	syscall

	# dodaje 1 do t1
	addi $t1, 1

	# wywołuje ponownie pętle
	j loop_wew

exit:
	# wypisuje out
	la $a0, out	
	li $v0, 4  
	syscall

	# koniec programu
	li $v0, 10
   	syscall
