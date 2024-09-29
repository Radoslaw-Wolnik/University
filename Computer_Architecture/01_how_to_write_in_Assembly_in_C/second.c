# include <stdio.h>

int main() {
    int x = 20;
    int y;

    
    // x += x -> 2x
    // 2x + 2x = 4x - move to diff register or memory
    // 4x+4x = 8x
    // 8x+8x = 16x
    // add 16x + 4x -> 20x
    
    // y = 20 * x;
    // wstwka in assembly: y = 20 * x
    asm (
        "mov eax, %1;"
        "add eax, eax;"
        "add eax, eax;"
        "mov ebx, eax;"
        "add eax, eax;"
        "add eax, eax;"
        "add eax, ebx;"
        "mov %0, eax;"
        : "=r" (y)
        : "r" (x) 
        : "eax", "ebx"
    );
    printf("x = %i, y = %i \n", x, y);
    return 0;
}

