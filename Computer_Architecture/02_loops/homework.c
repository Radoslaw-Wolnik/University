#include <stdio.h>
// gcc -masm=intel program_name.c -o out_name
// ./out_name

/* na maila wyslac piotr.szuca@ug.edu.pl
 * dzien przed kolejnymi laboratoriami do 23:59 koniecznie bo potem już nie uznaje
 * w trasci maila a nie w załączniku program
 * jesli cos jest zle to odsyła 
 * 
 * Znależć najdłuższy ciąg 1 w rozwinieciu binarnym liczby
 * eg 1010101011110101011101101
 *    1 1 1 1 1111 1 1 111 11 1
 *            here 
 * odpowiedź: 4
 *
 * eg 0x0F0FF0F0
 * F: 4 jedynki obok siebie
 *  tutaj 8
 * */
 
/*
 * basic solution - same as our but
 * 2 counters one with 1's and one with max lenght of 1's
 * if we have 0 then we zero the 1's counter
 * 
 * there are other solutions aparently
 * many of them
 * but all that matters is wheather it works or not - the solution doesn't matter (so dont get creative)
 * preatty much he solved it on the blackbord in class
 * */

// sprawdzian na papierze ale wiadomo ze robimy bledy na papierze wiec jesli bysmy to poprawili na komputerze w ciagu 1min to okay

/* cmp ecx, edx - compare licznik tymczasowy do licznika maxymalnego
 * ta operacja cale mnostwo flag
 * do testowania kilku flag jednoczesnie:
 * ja > a like above if 1'st is above 2'nd
 * jna not above tj <=
 * jb below < 
 * jnb not below >=
 * jae above or equal >= 
 * jbe belowe or equal <= 
 * */

/* bez znaku
 * ja  = jnbe  >
 * jna = jbe   <=
 * jb  = jnae  <
 * jnb = jae   >=
 * */
 
 /* z znakiem
  * ja  = jnle  >
  * jng = jle   <= 
  * jl  = jnge  <
  * jnl = jge   >=
  * */
  
  
void printBinary(unsigned int num) {
    // Determine the number of bits in an integer
    int num_bits = sizeof(num) * 8;
    
    // Loop through each bit from left to right
    for (int i = num_bits - 1; i >= 0; i--) {
        // Use bitwise AND with 1 to check the value of the bit at position i
        int bit = (num >> i) & 1;
        
        // Print the bit (either 0 or 1)
        printf("%d", bit);
    }
}

int main(int argc, char **argv) {
    int x = 0x2FDE4;
    // zapis szesnastkowy jest wygodny bo zamienia 4 bity na 1 liczbe
    int y;

    // kod w asemblerze - sprawdzamy maksymalna dlugosc ciagu 1 w liczbie binarnej
    // przesuwamy o 1 bit eax
    // sprawdzamy czy dalej cos jest w eax - czy 0
    // idziemy dalej 
    asm (
        "mov eax, %1;"
        "xor ebx, ebx;" // temporary 1's
        "xor ecx, ecx;" // max lenght 
        
        "petla:"
            "shl eax;" // przechodzimy 1 bit dalej; w fladze c mamy informacje czy byla tam 1 czy nie
            "jc przeskocz;" // jesli flaga jc jest zapalona - byla 1 to nie zeruj tymczasowego
            "xor ebx, ebx;"
            "jmp dontswitch;" // if we know its 0 then we can jump comparing current to max and go to checking if the rest is 0
            "przeskocz:"
                "inc ebx;" // increment ebx by 1
                "cmp ebx, ecx;" // compare temporary to max
                "jbe dontswitch;" // jump if current is below or equal to the max
                "mov ecx, ebx;" // jesli nie to zmien
                "dontswitch:"
                    "and eax, eax;" // eax AND eax - we check if there are any 1's left
                    "jnz petla;" // flaga zero in and if there were only 0's
    
        "mov %0, ecx;"
        
        : "=r" (y) // ouput referenced by %0
        : "r" (x) //  input referenced by %1
        : "eax", "ebx", "ecx" // registers that we will use
    );
    // jesli jest jakis blad w assemblerze to uwaza calosc tego co jest w asm("....") jako jedna linijke - tutaj line 11
    // skok w assemblerze nie moze byc wykonany o wiecej niz 127 bajtow do przodu lub 127 bajtow do tylu
    printf("x = %i, hex(x) = %x, y = %i\n", x, x, y);
    printf("Binary representation: ");
    printBinary(x);
    printf("\n");
    return 0;
}

