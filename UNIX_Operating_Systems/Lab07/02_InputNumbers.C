#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    // Uzytkownik wpisuje ile liczb nalezy pobrac
    printf("Wpisz ile liczb chcesz podac (int): ");
    scanf("%d", &n);

    // Sprawdz czy n jest poprawne
    if (n <= 0) {
        fprintf(stderr, "Niepoprawna liczba, nalezy podac liczbe dodatnia.\n");
        return 1;
    }

    FILE *negatywnyF, *pozytywnyF;

    // Otworz lub utworz pliki
    negatywnyF = fopen("ujemne.txt", "w");
    pozytywnyF = fopen("dodatnie.txt", "w");

    if (negatywnyF == NULL || pozytywnyF == NULL) {
        fprintf(stderr, "Niepoprawne otworzenie plikow\n");
        return 1;
    }

    int number;
    for (int i = 0; i < n; i++) {
        printf("Podaj liczbe calkowita #%d: ", i + 1);
        scanf("%d", &number);

        if (number == 0) {
            fprintf(stderr, "Error: Nie mozna podawac Zera, podaj dowolna inna calkowita liczbe.\n");
            fclose(negatywnyF);
            fclose(pozytywnyF);
            return 1; // Return an error code
        }

        if (number < 0) {
            fprintf(negatywnyF, "%d\n", number);
        } else {
            fprintf(pozytywnyF, "%d\n", number);
        }
    }

    fclose(negatywnyF);
    fclose(pozytywnyF);

    printf("Liczbby zostaly zapisane pomyslnie.\n");

    return 0;
}