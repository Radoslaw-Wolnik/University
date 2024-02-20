#include <unistd.h> // includes sleep()
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <time.h>


// global variables
pthread_mutex_t avaliable;


void UsePrinter(int pages, int empID){
    // shared resources
    printf("\n Job %d has started\n", empID); 
    for(int i = 0; i < pages; i++){
        sleep(1);
    }
    printf("\n Job %d has finished\n", empID); 

}


void *Employee(void *arg) {
    int empID = *((int *)arg);
    printf("My emp id: %d\n", empID);
    int DoIWantToUsePrinter = 0;
    unsigned int seed = (unsigned int)time(NULL);
    srand(seed);
    while(1){
        DoIWantToUsePrinter = rand() % 11 + 0; // liczby od 0 do 10
        if(DoIWantToUsePrinter == 7){
            pthread_mutex_lock(&avaliable);
            UsePrinter(rand() % 11 + 0, empID);
            pthread_mutex_unlock(&avaliable);
            // idk but mby locking and unlocking could be inside use printer? 
        }
        sleep(1);
    }
}


int main() {
    
    FILE *file;
    int empAmount;
    file = fopen("UnoNumero.txt", "r");

    if (file == NULL) {
        fprintf(stderr, "Nie udalo sie otworzysc pliku\n");
        return 1;
    }

    if (fscanf(file, "%d", &empAmount) != 1) {
        fprintf(stderr, "Nie udalo sie odczytac danych z pliku\n");
        fclose(file);
        return 10;
    }
    if (empAmount <= 0){
        fprintf(stderr, "Nieprawidlowa ilosc pracownikow\n");
        return 20;
    }
    fclose(file);
    int empIDs[empAmount];

    // ?? Can One do that ??
    pthread_t employees[empAmount]; 
    for(int i = 0; i < empAmount; i++){
        empIDs[i] = i;
        pthread_create(&employees[i], NULL, Employee, (void *)&empIDs[i]);
    }

    // nie ma warunku konca dla watkow employees -> nie ma warunku konca dla glownego programu
    // to end simply kill $!
    while(1){
        sleep(1);
    }

    return 0;
}