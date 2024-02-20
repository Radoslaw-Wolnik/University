#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>
#include <stdbool.h>
#include <sys/wait.h>
#include <signal.h>
// pthread_create - tworzy watek.
// pthread_join - czeka na zakonczenie watku.
// pthread_self - zwraca id watku.
// pthread_exit - konczy watek

pid_t UnoID;
pid_t DosID;
bool flag = 1;
bool kidsAlive = 0;
void handleSignalINT(int s) {
    // if there is a crash then child sends signal -SIGINT to parent
    flag = 0;
    printf("Crahs\n");
}

void handleSIGUSR1(int s) {
    // send by kiddoUno if it changed the light
    // pass it to kiddoDos
    if(kidsAlive){
        kill(DosID, SIGUSR2);
    }
    // there is boolan kidsAlive becouse theoreticly sb could send SIGUSR1/SIGUSR2 to main programm without it having kids yet
}

void handleSIGUSR2(int s) {
    // send by kiddoDos if it changed the light
    // pass it to kiddoUno
    if(kidsAlive){
        kill(UnoID, SIGUSR2);
    }
}


int main() {
    pid_t myID = getpid();
    const char *childUno = "./kiddoUno";
    const char *childDos = "./kiddoDos";
    // Set the seed for rand() using the current time
    srand((unsigned int)time(NULL));
    signal(SIGINT, handleSignalINT);
    signal(SIGUSR1, handleSIGUSR1);
    signal(SIGUSR2, handleSIGUSR2);
    

    const char *childMono = "./kiddoUno";
    pid_t InvokedKids[2];
    char *args[] = {NULL};
    // we use same child process, invoke it twice and exit to main body where we can do things on the invoked processes
    for (int i = 0; i < 2; ++i) {
        //pid_t pid = fork();
        InvokedKids[i] = fork();
        pid_t pid = InvokedKids[i];
        if (pid == -1) {
            perror("fork");
            exit(EXIT_FAILURE);
        }

        if (pid == 0) {
            // This is the child process
            execv(childMono, args);
            exit(EXIT_SUCCESS);
        }
    }

    UnoID = InvokedKids[0];
    DosID = InvokedKids[1];
    kill(UnoID, SIGUSR2);
    kill(UnoID, SIGUSR2);
    kidsAlive = 1;

    printf("%d : %d\n", InvokedKids[0], InvokedKids[1]);
    printf("%d : %d\n", UnoID, DosID);


    printf("The main body of program -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n");
    // main body : 
    int i = 0;
    while(flag){
        // rand zakres 1-2
        int randNum = rand() % 2 + 1;
        i += 1;
        printf("Curr iteration of rand int: %d\n", i);
        printf("parent: curr rand int: %d\n", randNum);
        if (randNum == 1){
            kill(UnoID, SIGUSR1);
        }
        if (randNum == 2){
            kill(DosID, SIGUSR1);
        }
        fflush(stdout);
        sleep(10);
    }

    // Ending alive children
    // as they run infinitely
    kill(UnoID, SIGTERM);
    kill(DosID, SIGTERM);
    
    return 0;
}
