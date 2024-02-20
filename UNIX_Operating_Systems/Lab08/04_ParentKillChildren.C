#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <time.h>
int main() {
    pid_t myID = getpid();
    const char *childUno = "./Z3kidUno";
    const char *childDos = "./Z3kidDos";
    
    printf("Im the parent\n");
    printf("Starting kiddos\n");

    pid_t UnoID = fork();
    if (UnoID == -1){
        printf("Sth wrong first fork\n");
        return 1;
    }
    if (UnoID == 0){
        execlp(childUno, childUno, (char *)NULL);
    }

    pid_t DosID = fork();
    if (DosID == -1){
        printf("Sth wrong scnd fork\n");
        return 1;
    }
    if (DosID == 0){
        execlp(childDos, childDos, (char *)NULL);
    }

    // here is main body
    // flags for kiddos
    char *UnoFlag = "y";
    char *DosFlag = "y";
    
    srand((unsigned int)time(NULL));
    while(UnoFlag == "y" || DosFlag == "y"){
        // rand zakres 1-50
        int randNum = rand() % 50 + 1;
        printf("Current random number: %d\n", randNum);
        if (randNum < 10){
            UnoFlag = "n";
            kill(SIGTERM, UnoID);
        }
        if (randNum > 40){
            DosFlag = "n";
            kill(SIGTERM, DosID);
        }
        sleep(1);
    }
    printf("Both kidds are dead\n");
    return 0;
}

