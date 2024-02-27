.data
msg: .asciiz	"Program wypisuje liczby od k do n co i:\n"
msg_k: .asciiz "Podaj k: "
msg_n: .asciiz "Podaj n: "
msg_i: .asciiz "Podaj i: "
m_okay: .asciiz "Okay, k jest mniejsze od n\n"
m_nope: .asciiz "nie okay, k nie jest mniejsze od n\nagain\n\n"
next_line: .asciiz "\n"
out: .asciiz	"koniec.\n\n"
						
.text
main:	
	# wypisuje msg -----------------
	la $a0, msg
	li $v0, 4  
	syscall

	# wypisuje msg_k ---------------
	la $a0, msg_k
	li $v0, 4  
	syscall

	# pobiera liczbe k
	li $v0, 5
	syscall
	
	# przypisuje t0 = k
	move $t0, $v0

	# wypisuje msg_n --------------
	la $a0, msg_n
	li $v0, 4  
	syscall

	# pobiera liczbe n
	li $v0, 5
	syscall
	
	# przypisuje t1 = n
	move $t1, $v0

	# wypisuje msg_i --------------
	la $a0, msg_i
	li $v0, 4  
	syscall

	# pobiera liczbe i
	li $v0, 5
	syscall
	
	# przypisuje t2 = i
	move $t2, $v0
	
	# sprawdza czy k jest mniejsze od n
	blt $t0, $t1, okay    # t0 < t1
	bgt $t0, $t1, nope    # t0 > t1

okay:
	# wypisuje m_okay
	la $a0, m_okay
	li $v0, 4  
	syscall

	# przechodzi do loop
	j loop

nope:
	# wypisuje m_nope 
	la $a0, m_nope
	li $v0, 4  
	syscall

	# przechodzi do main
	j main


loop:
	# porównuje t0 < t1 == k < n
	bgt $t0, $t1, exit

	# wypisuje 
   	move $a0, $t0
	li $v0, 1
    	syscall

	# next line 
	la $a0, next_line
	li $v0, 4  
	syscall
	
	# dodaje t2 do t0 == k += i
	add $t0, $t0, $t2

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
