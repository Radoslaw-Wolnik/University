// parent : parent : parent : parent : parent : parent : parent : parent : 

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <time.h>

const char *childUno = "./kidUno";
const char *childDos = "./kidDos";

char *UnoFlag = "y";
char *DosFlag = "y";

void handleUSR1(int s) {
    printf("Parent: recived SIGUSR1")
    UnoFlag = "n";
}

void handleUSR2(int s) {
    printf("Parent: recived SIGUSR2")
    DosFlag = "n";
}

int main() {
    // handle signals
    signal(SIGUSR1, handleUSR1);
    signal(SIGUSR2, handleUSR2);

    printf("Parent: Starting kiddos\n");

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

    printf("Parent: kids started succesfully\n");

    // wait until recived both signals
    while(UnoFlag == "y" || DosFlag == "y"){
        sleep(1);
    }

    kill(SIGTERM, UnoID);
    kill(SIGTERM, DosID);
    printf("Parent: Both kidds are dead\n");
    return 0;
}


// kidUno : kidUno : kidUno : kidUno : kidUno : kidUno : kidUno : kidUno : kidUno : 

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

void *LosujA(void *arg) {
    srand((unsigned int)time(NULL));
    int randDnum = 0
    while(1){
        randNum = rand() % 101 + 0;
        FILE *file = fopen("number1.txt", "a");
        if(file != NULL){
            fprintf(file, "%d\n", randNum);
            fclose(number1);
        }
        sleep(1);
    }
}

void *LosujB(void *arg) {
    srand((unsigned int)time(NULL));
    int randDnum = 0
    while(1){
        randNum = rand() % 101 + 0;
        FILE *file = fopen("number2.txt", "a");
        if(file != NULL){
            fprintf(file, "%d\n", randNum);
            fclose(number1);
        }
        sleep(1);
    }
}



int main() {
    
    printf("Kid Uno: Started, \n");

    // tworzenie pliku number1.txt
    FILE *number1 = fopen("number1.txt", "w");
    if (number1 == NULL) {
        fprintf(stderr, "Error creating the file number1.txt\n");
        return 1;
    }
    fclose(number1);

    // tworzenie pliku number2.txt
    FILE *number2 = fopen("number2.txt", "w");
    if (number2 == NULL) {
        fprintf(stderr, "Error creating the file number2.txt\n");
        return 1;
    }
    fclose(number2);

    pthread_t pierwszyWatek;
    pthread_t drugiWatek;
    pthread_create(&pierwszyWatek, NULL, LosujA, (void *));
    pthread_create(&drugiWatek, NULL, LosujB, (void *));

    // wait for threads
    if (pthread_join(pierwszyWatek, NULL) != 0) {
        fprintf(stderr, "Error joining thread pierwszyWatek.\n");
        return EXIT_FAILURE;
    }
    if (pthread_join(drugiWatek, NULL) != 0) {
        fprintf(stderr, "Error joining thread drugiWatek.\n");
        return EXIT_FAILURE;
    }


    return 0;
}

// kidDos : kidDos : kidDos : kidDos : kidDos : kidDos : kidDos : kidDos : kidDos :


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

pid_t parentID = getppid();

void *CheckA(void *arg) {
    while(1){
        FILE *file = fopen("number1.txt", "r");
        if(file != NULL){
            int number;
            if (fscanf(file, "%d", &number) != 1) {
                fprintf(stderr, "Nie udalo sie odczytac danych z pliku\n");
                fclose(file);
                return 10;
            }
            else{
                // check if every number in number is > 5
                flag = 1;
                for (int i = 0; i< number i++){
                    if ((number / 10 ** i ) % 5 + 5 == number){
                        // wieksze od 5
                    }
                    else{
                        flag = 0;
                    }
                }
                fclose(number1);
                if(flag == 1){
                    kill(SIGUSR1, parentID);
                }
            }
        }
        sleep(1);
    }
}

void *CheckB(void *arg) {
    while(1){
        FILE *file = fopen("number2.txt", "r");
        if(file != NULL){
            int number;
            if (fscanf(file, "%d", &number) != 1) {
                fprintf(stderr, "Nie udalo sie odczytac danych z pliku\n");
                fclose(file);
                return 10;
            }
            else{
                // check if every number in number is > 5
                flag = 1;
                for (int i = 0; i< number i++){
                    if ((number / 10 ** i ) % 5 == number){
                        // mniejsze od 5
                    }
                    else{
                        flag = 0;
                    }
                }
                fclose(number1);
                if(flag == 1){
                    kill(SIGUSR2, parentID);
                }
            }
        }
        sleep(1);
    }
}



int main() {
    
    printf("Kid Dos: Started, \n");

    pthread_t pierwszyWatek;
    pthread_t drugiWatek;
    pthread_create(&pierwszyWatek, NULL, CheckA, (void *));
    pthread_create(&drugiWatek, NULL, CheckB, (void *));

    // wait for threads
    if (pthread_join(pierwszyWatek, NULL) != 0) {
        fprintf(stderr, "Error joining thread pierwszyWatek.\n");
        return EXIT_FAILURE;
    }
    if (pthread_join(drugiWatek, NULL) != 0) {
        fprintf(stderr, "Error joining thread drugiWatek.\n");
        return EXIT_FAILURE;
    }


    return 0;
}

