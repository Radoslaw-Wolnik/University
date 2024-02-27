.data
msg1: .asciiz	"Program padaje najwiekszy wspolny dzielnik 2 liczb\n"
msg2: .asciiz	"Podaj pierwsza liczbe:\n"
msg3: .asciiz	"Podaj druga liczbe:\n"
wrong_input_mes: .asciiz "Zle podane liczby\n\n"
out: .asciiz	"Najwiekszy wspolny dzilenik to: "	
						
.text
main:	
	# wypisuje: "Program padaje najwiekszy wspolny dzielnik 2 liczb\n"
	la $a0, msg1	
	li $v0, 4  
	syscall


	# wypisuje: "Podaj pierwsza liczbe:\n"
	la $a0, msg2	
	li $v0, 4  
	syscall

	# pobiera pierwsza liczbe
	li $v0, 5
	syscall
	
	# przypisuje do $t0 = $v0
	move $t0, $v0

	# wypisuje: "Podaj druga liczbe:\n"
	la $a0, msg3	
	li $v0, 4  
	syscall
	
	# pobiera druga liczbe
	li $v0, 5
	syscall
	
	# przypisuje do $t1 = $v0
	move $t1, $v0
	
	# sprawdza czy obie liczby sa wieksze od zera
	ble $t0, 0, wrong_input
	ble $t1, 0, wrong_input

	j wyznacz_nwd


wrong_input:
	# wypisuje wrong_input_mes
	la $a0, wrong_input_mes
	li $v0, 4  
	syscall
	j main



	# jesli t0 = t1 to przeskakuje do exit
	# jesli t0 jest wieksze od t1 to przeskakuje do wieksze w ktorym 
	# t0 = t0 - t1
	# jesli t0 nie jest wieksze to znaczy ze t1 jest wieksze wiec wykonuje
	# t1 = t1 - t0

wyznacz_nwd:
	beq $t0, $t1, exit
	bgt $t0, $t1, wieksze
	sub $t1, $t1, $t0
	j wyznacz_nwd

wieksze:
	sub $t0, $t0, $t1
	j wyznacz_nwd


exit:
	# wypisuje out
	la $a0, out	
	li $v0, 4  
	syscall

	# wypisuje nwd
   	move $a0, $t0
	li $v0, 1
    	syscall

	# koniec programu
	li $v0, 10
   	syscall