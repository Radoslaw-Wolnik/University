// IA - 32 STACK RTL 
.intel_syntax noprefix
.global main // zeby linker widzial na zewnatrz main bo wszystkie funkcje w asemblerze sa wewnetrzne
.text // teraz text programu - beda pnoniki
main:
mov eax, OFFSEY mesg // w eax mamy wskaźnik na pierwszy znak naszej wiadomosci
// wolamy printf a na stosie sa argumenty dla prontf
// wiec kladziemy na stos nasza wiadomosc
push eax // kladziemy na stos eax
// wolajac printf skaczemy do printf i musimy podac gdzie wrocic
call printf // wolamy print i wracamy tutaj po wykonaniu go
pop eax // zdejmij ze stosu do eax ?
mov eax, 0 // pierwszy rejestr jest tym co zwracamy
ret

// nasze dane
.data
mesg: // etykieta - zmienna ktora ma nasz napis
.asciz "Hello World\n" // nasz napis


/* funkcja printf potrafi wszystko
 * trzeba poprosic system o wszystko
 * na razie bedziemy pracowac na 32 bit system bo jest prosciej 
 * binary calling interface - ABI aplication binary interface
 * IA - 32
 */ 

/* pierwsze wersje fortrana nie mialy stosu i nie mozna bylo robic rekurencji
 * bo przekazywano argumenty do funkcji i sie nadpisywala
 * chyba bedziemy przekazywac do printf stos i printf bedzie z niego czytac
 * [wierzcholek stosu]
 * [   rośnie w dół  ]
 * [       ....      ]
 * [       ....      ]
 * [   rosna w gore  ]
 * [   dane progrmu  ]
 * [   kod programu  ]
 * [   kod programu  ]
 * [   kod programu  ]
 */


// to compile:
// gcc -m32 name.s -o my_out_name
// library gcc multilib to compile with gcc as 32 bit programs
// po kompilacji:
// > warning: creating DT_TEXTREL in a PIE
// that we can just ignore 

// bez komentarzy :
.intel_syntax noprefix
.global main
.text 
main:
mov eax, OFFSEY mesg 
push eax 
call printf
pop eax
mov eax, 0
ret

.data
mesg:
.asciz "Hello World\n"
