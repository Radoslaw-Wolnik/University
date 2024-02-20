#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    // Create pipes
    int pipe1[2];
    int pipe2[2];

    if (pipe(pipe1) == -1 || pipe(pipe2) == -1) {
        perror("Error creating pipes");
        exit(EXIT_FAILURE);
    }

    // Fork a child process
    pid_t child_pid = fork();

    if (child_pid == -1) {
        perror("Error forking");
        exit(EXIT_FAILURE);
    }

    if (child_pid == 0) {
        // Child process
        close(pipe1[1]); // Close write end of pipe1
        close(pipe2[1]); // Close write end of pipe2

        // Redirect stdin for the first file
        dup2(pipe1[0], STDIN_FILENO);
        close(pipe1[0]);

        // Redirect stdout for wc command
        dup2(pipe2[1], STDOUT_FILENO);
        close(pipe2[0]);

        // Execute the wc command to count words
        execlp("wc", "wc", "-w", (char *)NULL);
        perror("Error executing wc");
        exit(EXIT_FAILURE);
    } else {
        // Parent process
        close(pipe1[0]); // Close read end of pipe1
        close(pipe2[1]); // Close write end of pipe2

        // Open the files for reading
        FILE *file1 = fopen("file1.txt", "r");
        FILE *file2 = fopen("file2.txt", "r");

        if (!file1 || !file2) {
            perror("Error opening files");
            exit(EXIT_FAILURE);
        }

        char buffer[4096];
        size_t bytesRead;

        // Read from file1 and write to pipe1
        while ((bytesRead = fread(buffer, 1, sizeof(buffer), file1)) > 0) {
            write(pipe1[1], buffer, bytesRead);
        }

        // Close write end of pipe1
        close(pipe1[1]);

        // Read from file2 and write to pipe1
        while ((bytesRead = fread(buffer, 1, sizeof(buffer), file2)) > 0) {
            write(pipe1[1], buffer, bytesRead);
        }

        // Close write end of pipe1
        close(pipe1[1]);

        // Close file streams
        fclose(file1);
        fclose(file2);

        // Wait for the child process to finish
        wait(NULL);

        // Read from pipe2 to get the word count result
        char result[64];
        ssize_t count = read(pipe2[0], result, sizeof(result));

        if (count > 0) {
            result[count] = '\0';
            printf("The file with more words is: %s", result);
        } else {
            perror("Error reading from pipe");
        }

        // Close read end of pipe2
        close(pipe2[0]);
    }

    return 0;
}
