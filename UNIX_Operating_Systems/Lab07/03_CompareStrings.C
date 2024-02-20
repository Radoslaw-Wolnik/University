#include <stdio.h>
#include <string.h>

int main() {
    char str1[100], str2[100];

    printf("Podaj pierwszy napis: ");
    scanf("%s", str1);

    printf("Podaj drugi napis: ");
    scanf("%s", str2);

    FILE *wczesniejszyPlik, *dluzszyPlik;

    // Open files for writing
    wczesniejszyPlik = fopen("wczesniej.txt", "w");
    dluzszyPlik = fopen("dluzszy.txt", "w");

    if (wczesniejszyPlik == NULL || dluzszyPlik == NULL) {
        fprintf(stderr, "Nie udalo sie otworzyc plikow\n");
        return 1;
    }

    // Sprawdz ktory jest pierwszy
    int wczesniej = strcmp(str1, str2);
    if (wczesniej < 0) {
        fprintf(wczesniejszyPlik, "%s\n", str1);
    } 
    else if (wczesniej > 0) {
        fprintf(wczesniejszyPlik, "%s\n", str2);
    } 
    else {
        fprintf(stderr, "Napisy sa identyczne.\n");
        fclose(wczesniejszyPlik);
        fclose(dluzszyPlik);
        return 1;
    }

    // Sprawdz ktory jest dluzszy
    int dlugoscOba = strlen(str1) - strlen(str2);
    if (dlugoscOba > 0) {
        fprintf(dluzszyPlik, "%s\n", str1);
    } 
    else if (dlugoscOba < 0) {
        fprintf(dluzszyPlik, "%s\n", str2);
    } 
    else {
        fprintf(stderr, "Error: Napisy sa tej samej dlugosci.\n");
        fclose(wczesniejszyPlik);
        fclose(dluzszyPlik);
        return 1;
    }

    fclose(wczesniejszyPlik);
    fclose(dluzszyPlik);

    return 0;
}
