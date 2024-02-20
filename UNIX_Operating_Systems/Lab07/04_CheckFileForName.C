#include <stdio.h>
#include <string.h>

// funkcja sprawdzajaca czy napis ma tylko ma literki
int isAlphabetic(const char *str) {
    while (*str) {
        char ch = *str;
        if (!((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z'))) {
            return 0;
        }
        str++;
    }
    return 1; // wszystko ok
}

int main() {
    char name[50], surname[50];
    char buffer[100];

    printf("Enter name: ");
    scanf("%s", name);

    printf("Enter surname: ");
    scanf("%s", surname);

    if (!isAlphabetic(name) || !isAlphabetic(surname)) {
        fprintf(stderr, "Error: Name and surname should contain only letters.\n");
        return 1;
    }

    FILE *file = fopen("baza.txt", "r");

   
    if (file == NULL) {
        fprintf(stderr, "Error opening the file\n");
        return 1;
    }

    int found = 0;

    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        // Separate the line into name and surname
        char file_name[50], file_surname[50];
        sscanf(buffer, "%s %s", file_name, file_surname);

        if (strcmp(name, file_name) == 0) {
            found = 1;
            break;
        }
    }

    fclose(file);

    if (found) {
        printf("The name %s is in the file.\n", name);
    } else {
        printf("The name %s is not in the file.\n", name);
    }

    return 0;
}
