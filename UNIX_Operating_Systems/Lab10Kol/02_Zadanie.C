#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <time.h>


// global variables
pthread_mutex_t avaliable = PTHREAD_MUTEX_INITIALIZER;
sem_t semafor; // max avaliable 3
int global = 0;


void *Thread(void *arg) {
    int ThreadID = *((int *)arg);
    printf("Thread started, my id: %d\n", ThreadID);
    int doLoop = 1;
    int ModifyNumber = 0;
    unsigned int seed = (unsigned int)time(NULL);
    srand(seed);
    
    // semafor wait for avaliability - max 3 threads
    // semafor take one space
    sem_wait(&semafor);
    
    while(doLoop == 1){
        ModifyNumber = rand() % 101 + 0; // liczby od 0 do 10        
        // change number
        pthread_mutex_lock(&avaliable);
        global = ModifyNumber;
        pthread_mutex_unlock(&avaliable);

        // wait 20s
        sleep(20);
        if(global == ModifyNumber){
            doLoop = 0;
        }    
    }
    // zwolnij semafor - koniec dzialania
    sem_post(&semafor);
    
    printf("Thread %d ended\n", ThreadID);
}


int main() {

    int amount = 10;

    // Create Semafor
    sem_init(&semafor, 0, 3);
    // Creating Threads
    pthread_t threads[amount]; 
    int threadIDs[amount];
    for(int i = 0; i < amount; i++){
        threadIDs[i] = i;
        pthread_create(&threads[i], NULL, Thread, (void *)&threadIDs[i]);
    }


    // Wait for threads to finish
    for (int i = 0; i < amount; ++i) {
        if (pthread_join(threads[i], NULL) != 0) {
            fprintf(stderr, "Error joining thread %d.\n", i);
            return EXIT_FAILURE;
        }
    }

    // destroy mutex
    if (pthread_mutex_destroy(&avaliable) != 0) {
        perror("Failed to destroy mutex");
        return 1;
    }

    // destroy semafor
    if (sem_destroy(&semafor) != 0) {
        perror("Failed to destroy semaphore");
        return 1;
    }


    printf("Main thread completed.\n");
    return 0;
}
