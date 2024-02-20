#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>

// pthread_create - tworzy watek.
// pthread_join - czeka na zakonczenie watku.
// pthread_self - zwraca id watku.
// pthread_exit - konczy watek

void *myThread(void *arg) {
    int randNum = 21;
  
    while((randNum % 5) != 0){
        // rand zakres 1-50
        pthread_t tid = pthread_self();
        randNum = rand() % 50 + 1;
        printf("My threadID: %lu \n", tid);
        printf("Current random number: %d\n", randNum);
        sleep(1);
    }
}


int main() {
    // zmienna typu Id of thread
    pthread_t threadID;
    // tworzy thread z funkcji myThread i przypisuje ID do threadID
    pthread_create(&threadID, NULL, myThread, NULL);
    // czeka na zakoncznie threadID
    pthread_join(threadID, NULL);

return 0;
}
