# include <stdio.h>
// enviorement in linux installed 
// geany file_name.c &
// gcc file_name.c -o out_file_name
// gcc file_name.c -> a.out


// procesory x86 maja dwie skladnie assembly - skladnia intela i skladnia miedzynarodowa - ATAT
// domyslnie gcc kompiluje ATAT wiec bedziemy zmieniac
// roznice eg:
// intel: mov eax, ebx; skopiuj zawartosc ebx do eax  ;; cel, zrodlo
// ATAT : movl ebx, eax; l mowi ze operandy sa 32 bit ;; zrodo, cel   
// gcc -masm=intel file_name.c -o out_name

// gcc -masm=intel -save-temps file_name.c
// a-first.s - in assembly compiled code

int main() {
    int x = 2024;
    int y;
    // kompilator zarzadza tym jakie zmienne są w rejestrze
    // zeby zrobic operacje na zmiennej (dowolna operacje) musi byc w rejestrze
    // jesli zmienna nie jest uzywana to moze zostac przeniesiona do pamieci
    // ale zeby wykonac na niej operacje kompilator przeniesie ja spowrotem do rejestru
    
    // wobec tego jak piszemy wstawke w assemblerze musimy najpierw zadeklarowac dla kompilatora co ona robi
    // po to zeby kompilator zwolnil potrzebne nam rejestry - zmienne sa albo w rejestrze albo w pamieci
    // uzywajac rejestru mozemy nadpisac jakas zmienna gdybysmy nie zadeklarowali ze bedziemy go uzywac
    
    // gcc -O[0-3] zmienia optymalizacje O0 standardowa
    // O1 optymalizuje po to by zuzywac jak najmniej pamieci
    // O2 optymalizacja nastawiona na czas wykonania
    // O3 optymalizacja agresywna - kompilator nie przejmuje sie niczym ale ma byc jak najszybsze wykonanie
    // w przypadku kompilacji agresywnej tracimy struktore kodu w assemblerze - moze zmienic kolejnosc linijek ;; tracimy debug
    
    
    // w C jesli napiszemy 
    // "A"
    // "B"
    // "C"
    // to to samo co "ABC"
    
    // nowa linijka jako \n "kod kod kod \n"
    // lub nowa linijka   ; "kod kod kod  ;"
    
    
    // y = x + x;
    // wstwka in assembly: y = x + x
    asm (
        "mov eax, %1;"
        "add eax, eax;"
        "mov %0, eax;"
        : "=r" (y)
        : "r" (x) 
        : "eax", "ebx"
    );
    // "kod w assemblerze"
    // : wyjscie - gdzie zapisac wyjscie naszej wstawki
    // : wejscie do naszej wstawki - co potrzebujemy z programu; w tej linijce piszemy co czytamy, "r" - register - zostanie zapisane do jakiegos rejestru, "m" - memory
    // : w ostatniej linijce lista rejestrow jakich uzywamy
    
    // skad wiemy ktore rejestry - od lewej do prawej z gory na dol
    // %0 pierwszy %1 drugi %2 trzeci itd
    
    
    // po  co pisac w assemblerze?
    // 1. kiedy chcemy miec dostep do nietypoiwego sprzetu
    // 2. tworcy sysemu komputerowego - opchrona, pamiec etc sa w specjalnych rejestrach i zeby do takiego rejestru miec dostep to trzeba uzyc assembly
    printf("x = %i, y = %i \n", x, y);
    return 0;
}

// hp klawiatura całkiem miła 
