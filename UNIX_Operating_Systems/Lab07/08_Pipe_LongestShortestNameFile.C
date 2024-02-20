#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <limits.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

#define PIPE_NAME "/tmp/names_pipe"

// Function to find the longest or shortest name and write it to the FIFO
void find_and_write(const char *fifo_name, int (*compare)(size_t, size_t)) {
    mkfifo(fifo_name, 0666);

    int fifo_fd = open(fifo_name, O_WRONLY);
    if (fifo_fd == -1) {
        perror("Error opening FIFO");
        exit(EXIT_FAILURE);
    }

    DIR *dir = opendir("/path/to/your/home/directory");
    if (dir == NULL) {
        perror("Error opening the directory");
        exit(EXIT_FAILURE);
    }

    size_t result_length = compare(0, SIZE_MAX);
    char result_name[PATH_MAX];

    struct dirent *entry;

    while ((entry = readdir(dir)) != NULL) {
        if (entry->d_type == DT_REG || entry->d_type == DT_DIR) {
            size_t name_length = strlen(entry->d_name);

            if (compare(name_length, result_length)) {
                result_length = name_length;
                strcpy(result_name, entry->d_name);
            }
        }
    }

    closedir(dir);

    write(fifo_fd, result_name, strlen(result_name) + 1);

    close(fifo_fd);
}

int main() {
    pid_t child_pid;

    child_pid = fork();

    if (child_pid == -1) {
        perror("Error forking");
        exit(EXIT_FAILURE);
    } else if (child_pid == 0) {
        // Child process for finding the names
        find_and_write(PIPE_NAME, (int (*)(size_t, size_t))(&more_than));
        find_and_write(PIPE_NAME, (int (*)(size_t, size_t))(&less_than));
        exit(EXIT_SUCCESS);
    } else {
        // Parent process
        int status;
        waitpid(child_pid, &status, 0);

        // Read the results from the FIFO
        char longest_name[PATH_MAX];
        char shortest_name[PATH_MAX];

        int fifo_fd = open(PIPE_NAME, O_RDONLY);
        if (fifo_fd == -1) {
            perror("Error opening FIFO for reading");
            exit(EXIT_FAILURE);
        }

        read(fifo_fd, longest_name, sizeof(longest_name));
        read(fifo_fd, shortest_name, sizeof(shortest_name));

        close(fifo_fd);

        // Display the results
        printf("Longest name: %s\n", longest_name);
        printf("Shortest name: %s\n", shortest_name);

        // Remove the FIFO
        unlink(PIPE_NAME);
    }

    return 0;
}
