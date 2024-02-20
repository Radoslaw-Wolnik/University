#include <stdio.h>
#include <stdlib.h>

int main() {
    // Menu
    printf("1. Delete przedmioty.txt\n");
    printf("2. Copy przedmioty.txt to Other folder\n");
    printf("3. Move przedmioty.txt to Other folder\n");
    printf("Enter your choice (1, 2, or 3): ");

    int choice;
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            // Delete przedmioty.txt
            if (rm("przedmioty.txt") == 0) {
                printf("File przedmioty.txt deleted successfully.\n");
            } else {
                fprintf(stderr, "Error deleting file przedmioty.txt\n");
            }
            break;

        case 2:
            // Cp przedmioty.txt to Other folder unix cp win copy
            if (system("cp przedmioty.txt Other\\") == 0) {
                printf("File przedmioty.txt copied to Other folder successfully.\n");
            } else {
                fprintf(stderr, "Error copying file przedmioty.txt\n");
            }
            break;

        case 3:
            // Move przedmioty.txt to Other folder
            if (mv("przedmioty.txt", "Other\\przedmioty.txt") == 0) {
                printf("File przedmioty.txt moved to Other folder successfully.\n");
            } else {
                fprintf(stderr, "Error moving file przedmioty.txt\n");
            }
            break;

        default:
            fprintf(stderr, "Invalid choice. Please enter 1, 2, or 3.\n");
            return 1;
    }

    return 0;
}
