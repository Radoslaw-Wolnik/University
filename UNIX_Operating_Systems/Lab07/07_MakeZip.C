#include <stdio.h>
#include <stdlib.h>

int main() {
    // Menu
    printf("Choose an option:\n");
    printf("1. Create a .tar archive for the 'temp' folder\n");
    printf("2. Create a .zip archive for the 'temp' folder\n");
    printf("Enter your choice (1 or 2): ");

    int choice;
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            // Create a .tar archive for the 'temp' folder
            if (system("tar -cvf temp.tar temp") == 0) {
                printf("Archive temp.tar created successfully.\n");
            } else {
                fprintf(stderr, "Error creating archive temp.tar\n");
            }
            break;

        case 2:
            // Create a .zip archive for the 'temp' folder
            if (system("zip -r temp.zip temp") == 0) {
                printf("Archive temp.zip created successfully.\n");
            } else {
                fprintf(stderr, "Error creating archive temp.zip\n");
            }
            break;

        default:
            fprintf(stderr, "Invalid choice. Please enter 1 or 2.\n");
            return 1; // Return an error code
    }

    return 0;
}
