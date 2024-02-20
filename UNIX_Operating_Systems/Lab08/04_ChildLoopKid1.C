#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main() {
    pid_t myID = getpid();
    pid_t parentID = getppid();
    while(1){
        
        printf("Im kiddo Uno\n");
        printf("My ID: %d \n", myID);
        printf("ID of my parent: %d \n", parentID);
        sleep(1);
    }

    return 0;
}

