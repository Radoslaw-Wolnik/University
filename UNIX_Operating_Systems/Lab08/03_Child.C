#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// getpid - zwraca identyfikator biezaego procesu.
// getppid - zwraca identyfikator nadrzednego procesu.
// sleep - zawiesza wykonanie procesu na pewien czas

int main() {
    int randNum = 21;
    pid_t myID = getpid();
    pid_t parentID = getppid();
    
    printf("My ID: %d, \n", myID);
    printf("ID of my parent: %d, \n", parentID);

    while((randNum % 50) != 0){
        // rand zakres 1-50
        randNum = rand() % 50 + 1;
        printf("Current random number: %d\n", randNum);
        sleep(1);
    }

    return 0;
}