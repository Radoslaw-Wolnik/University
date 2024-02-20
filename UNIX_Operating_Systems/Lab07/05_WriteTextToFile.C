#include <stdio.h>

int main() {

    FILE *file = fopen("przedmioty.txt", "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening the file for writing\n");
        return 1;
    }

    fprintf(file, "Informatyka\nMatematyka\nJezyk angielski\n");
    fclose(file);
    printf("Content written to przedmioty.txt successfully.\n");

    return 0;
}