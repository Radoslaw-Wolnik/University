// gcc Zadanie3.c -o za3 -lm 
// becouse of math.h library
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <unistd.h>

//int EXIT_FAILURE = 11;

int threadNum = 0;
pthread_barrier_t my_barrier;
pthread_barrier_t scnd_barrier;

void reset_barrier() {
    // Destroy the existing barrier
    pthread_barrier_destroy(&my_barrier);

    // Initialize a new barrier
    pthread_barrier_init(&my_barrier, NULL, threadNum);
}


void *thRozklad(void *arg) {
    int number = *(int *)arg;
    int beginning = number;
    char result[100] = "";
    printf("There is many of us: %d\n", number);

    // Perform some work before reaching the barrier
    printf("Wait 1\n");
    // Wait for all threads to reach the barrier
    int barrier_result = pthread_barrier_wait(&my_barrier);
    
    // Check if this thread is the one to release others from the barrier
    //if (barrier_result == PTHREAD_BARRIER_SERIAL_THREAD) {
    //    reset_barrier();
    //}
    printf("Start mathing\n");

    // ROZKLAD LICZBY NA LICZBY PIERWSZE
    int k = 0;
    while(number != 1){
        printf("Do dod odododo %d \n", number);
        int div = 0;
        int prev = number;
        double limit = ceil(sqrt(number)) + 1;
        if ( number % 2 == 0){
            div = 2;
            number = number/2;
        }
        else{
        for(int i = 3; i < (int)limit; i+=2){
            if(number%i == 0){
                div = i;
                number = number /i;
                break;
            }
        }}
        // nasza liczba jest pierwsza
        if(number == prev){
            div = number;
            number = number/number;
        }
        char numChar[4];
        snprintf(numChar, sizeof(numChar), "%d", div);
        printf("div: %d, number: %d, prev: %d\n", div, number, prev);
        strcat(result, numChar);
        strcat(result, ", ");
        printf("result: %s\n", result);
        k+=1;
    }
    printf("Wait 2\n");

    // kolejna barrier
    // wait
    barrier_result = pthread_barrier_wait(&scnd_barrier);
    printf("All Waited\n");
    // Wypisz solution
    printf("Rozklad liczby: %d na czynniki to: %s \n", beginning, result);
    return NULL;
}



int main() {

    // open file and read to determine the ammount of numbers
    FILE *file = fopen("threeNumbers.txt", "r");
    
    if (file == NULL) {
        fprintf(stderr, "Unable to open the file.\n");
        return 1;
    }

    int currentNumber = 0;
    // Read each number from the file
    while (fscanf(file, "%d", &currentNumber) == 1) {
        threadNum += 1;
    }
    printf("Main: Number of threads: %d\n", threadNum);

    // Reset the file position indicator to the beginning
    fseek(file, 0, SEEK_SET);
    
    pthread_t threads[threadNum];
    int numbers[threadNum];
    int i = 0;
    while (fscanf(file, "%d", &currentNumber) == 1) {
        numbers[i] = currentNumber;
        i++;
    }

    fclose(file);


    printf("Main: numbers saved to array\n");

    // Initialize the my_barrier with the number of threads
    if (pthread_barrier_init(&my_barrier, NULL, threadNum) != 0) {
        perror("Error initializing barrier");
        return EXIT_FAILURE;
    }

    // Initialize the scnd_barrier with the number of threads
    if (pthread_barrier_init(&scnd_barrier, NULL, threadNum) != 0) {
        perror("Error initializing barrier");
        return EXIT_FAILURE;
    }


    // Create threads
    for (int i = 0; i < threadNum; ++i) {
        if (pthread_create(&threads[i], NULL, thRozklad, (void *)&numbers[i]) != 0) {
            fprintf(stderr, "Error creating thread %d.\n", i);
            return EXIT_FAILURE;
        }
    }
   //while(1){
   //   sleep(1);
   //}


    // Wait for threads to finish
    for (int i = 0; i < threadNum; ++i) {
        if (pthread_join(threads[i], NULL) != 0) {
            fprintf(stderr, "Error joining thread %d.\n", i);
            return EXIT_FAILURE;
        }
    }


   // Destroy the barriers
   if (pthread_barrier_destroy(&my_barrier) != 0) {
        perror("Error destroying MY barrier");
        return EXIT_FAILURE;
   }
   if (pthread_barrier_destroy(&scnd_barrier) != 0) {
        perror("Error destroying SCND barrier");
        return EXIT_FAILURE;
   }

    printf("Main thread completed.\n");

    return 0;
}
