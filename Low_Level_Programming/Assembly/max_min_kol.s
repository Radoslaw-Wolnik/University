.data
msg1: .asciiz	"Program Podaje najwieksza i najmniejsza liczbe z wszytkich liczb ktore poda uzytkownik:\n"
first: .asciiz	"Podaj pierwsza liczbe:\n"
next: .asciiz	"Czy chcesz podac kolejna liczbe?[1/0]\n"
num_next: .asciiz	"Podaj liczbe:\n"
out1: .asciiz "Maksymalna liczba: "
out2: .asciiz "\nMinimalna liczba: "	
						
.text
main:	
	# wypisuje msg1
	la $a0, msg1	
	li $v0, 4  
	syscall

	# wypisuje first
	la $a0, first	
	li $v0, 4  
	syscall

	# pobiera pierwsza liczbe
	li $v0, 5
	syscall
	
	move $t0, $v0    # $t0 max
	move $t1, $v0    # $t1 min
	
	j dalej

dalej:
	# wypisuje czy chcesz dalej
	la $a0, next	
	li $v0, 4  
	syscall

	# pobiera czy dalej
	li $v0, 5
	syscall

	beq $v0, 0, exit
	beq $v0, 1, next_true

next_true:
	# wypisuje num_next
	la $a0, num_next	
	li $v0, 4  
	syscall

	# pobiera liczbe
	li $v0, 5
	syscall
	
	bgt $v0, $t0, max
	blt $v0, $t1, min
	j dalej

max:
	move $t0, $v0    # $t0 max
	j dalej

min:
	move $t1, $v0    # $t1 min
	j dalej

exit:
	# wypisuje out1
	la $a0, out1	
	li $v0, 4  
	syscall

	# wypisuje max = $t0
   	move $a0, $t0
	li $v0, 1
    	syscall

	# wypisuje out2
	la $a0, out2	
	li $v0, 4  
	syscall
	
	# wypisuje min = $t1
   	move $a0, $t1
	li $v0, 1
    	syscall

	# koniec programu
	li $v0, 10
   	syscall