include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file;
    int number;
    int max, min;
    
    file = fopen("liczby.txt", "r");

    if (file == NULL) {
        fprintf(stderr, "Nie udalo sie otworzysc pliku\n");
        return 1;
    }

    if (fscanf(file, "%d", &number) != 1) {
        fprintf(stderr, "Nie udalo sie sczytac czegokolwiek z pliku\n");
        fclose(file);
        return 1;
    }

    max = number;
    min = number;

    // Loop through the rest of the numbers in the file
  while (fscanf(file, "%d", &number) == 1) {
        // Update largest and smallest
        if (number > max) {
            max = number;
        } else if (number < min) {
            min = number;
        }
    }

    fclose(file);

    // Display the results
    printf("Largest number: %d\n", max);
    printf("Smallest number: %d\n", min);

    return 0;
}