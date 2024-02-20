#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <time.h>
#include <unistd.h>

//global variables

sem_t semafor; // max value 5
// semaphore cant get negative numbers although doing wait (decreasing val) on 0 yelds exception (CHYBA)
// MAX VALUE OF 5 CAN BE DEFINED AS CONSTANT


// Semaphores are typically used to control access to a shared resource or protect a critical section. 
// The value often represents the number of available units of that resource.


void *Producent(){
    unsigned int seed = (unsigned int)time(NULL);
    srand(seed); // setting seed for rand
    // losuj liczbe
    // jesli wynos == 2 to stworz produkt
    int create = 0;
    int current_value;
    while(1){
        create = rand() % 11 + 0; // liczby od 0 do 10
        if(create == 2){
            sem_getvalue(&semafor, &current_value);
            // if semafor == 5
            // wait - sleep - az sie zmniejszy i potem dodaj
            if(current_value == 5){
                while(current_value == 5){
                    sleep(1);
                    sem_getvalue(&semafor, &current_value);
                }
            }
            // otherwise dodaj od razu
            sem_post(&semafor);
            printf("Producent: Cookie created\n");
        }
        sleep(1);
    }
}


void *Konsumer(){
    unsigned int seed = (unsigned int)time(NULL);
    srand(seed); // setting seed for rand
    // losuj liczbe 
    // jesli wynosi == 7 to zjedz produkt - decrese semafor value
    int eat = 0;
    while(1){
        eat = rand() % 11 + 0; // liczby od 0 do 10
        if(eat == 7){
            sem_wait(&semafor);
            printf("Konsumer: Cookie eaten\n");
        }
        // if semafor == 0
        // wait az sie zwiekszy i potem odejmij - wbudowane
    }
    sleep(1);
}


int main() {
    FILE *file;
    int fileNum[2];
    
    file = fopen("liczbaProducentowKonsumerow.txt", "r");

    if (file == NULL) {
        fprintf(stderr, "Nie udalo sie otworzysc pliku\n");
        return 1;
    }

    for(int i = 0; i < 2; i++){
        if (fscanf(file, "%d", &fileNum[i]) != 1) {
            fprintf(stderr, "Nie udalo sie odczytac danych z pliku\n");
            fclose(file);
            return 10;
        }
        if(fileNum[i] <= 0){
            fprintf(stderr, "Nieprawidlowa wartosc w pliku\n");
            fclose(file);
            return 20;
        }
    }
    fclose(file);

    /*
    int sem_init(
        sem_t *sem          // pointer to semaphore variable    ,
        int pshared         // If = 0: can be used in threads only, else in process,
        unsigned int value  // initial value of the semaphore counter
    );
    return value 0 on successful & -1 on failure
    */

    sem_init(&semafor, 0, 3);
    
    
    // fileNum[0] ilosc producentow
    // fileNum[1] ilosc konsumentow

    pthread_t producents[fileNum[0]]; 
    for(int i = 0; i < fileNum[0]; i++){
        pthread_create(&producents[i], NULL, Producent, NULL);
        sleep(3);
    }

    pthread_t konsumers[fileNum[0]]; 
    for(int i = 0; i < fileNum[0]; i++){
        pthread_create(&konsumers[i], NULL, Konsumer, NULL);
        sleep(3);
    }


    // to end simply kill $! or Ctrl+C
    while(1){
        int current_value;
        sem_getvalue(&semafor, &current_value);
        printf("Main: Current semaphore val = %d\n", current_value);
        sleep(1);

    }
    return 0;
}
