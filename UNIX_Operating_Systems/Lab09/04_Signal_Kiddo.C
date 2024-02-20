// exec name: kiddoUno
// SIGUSR1 send to parentID - changed light - another kid can change light
// SIGINT to parent if crash occured
// SIGUSR1 - create new car
// SIGUSR2 - change canChange light - another kid changed lioght and parrent communicates that to us

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>
#include <stdbool.h>
#include <signal.h>

bool light = 0;
bool canChange = 1; // in second child set as 1
int road[50];
const int roadLen = sizeof(road) / sizeof(road[0]);

void *lightThread(void *arg) {
    // thread symuliting trafic Lights 
    // every 10s lights change state
    // 0 : false : red light
    // 1 : true : green light
    // either light can be passed in incantation of function or be a global var
    pid_t parentID = getppid();
    while(1){
        // if changed state send signal to parent that changed state
        // parent will pass it to the second child
        // child will only change state if it got signal that another child changed state
        // one child begins with red light, one begins with green light
        if(canChange){
            light = !light;
            //kill(parentID, SIGUSR1);
            canChange = 1;
        }
        //thread.moveCars zalezy od light
        sleep(2);
    }

}


int moveCars(){
    // function gets list of int[50]
    // if road[i] = 0 : puste pole
    // if road[i] != 0 : there is car here
    // cars move with speed 1 - 10
    // number tells how much car moves forward ;; 1 : 1 cell forward ;; 2 : 2 cells forward etc

    if(road[0] != 0){
        road[0] = 0;
    }
    int prevCar = -100;
    // move the rest of cars
    for(int i = 1; i < roadLen; i++){
        if(road[i] != 0){

            int newPlace = i - 1;
            // sprawdzenie czy "przeskoczylo" inne auto - kraksa
            if(newPlace < prevCar){
                return 1;
            }
            // wyjechalo
            else if(newPlace < 0){
                road[i] = 0;
            }
            // przesun do przodu
            else{
                road[newPlace] = road[i];
                road[i] = 0;
                prevCar = newPlace;
            }
        }
    }
    return 0;
}

void *roadThread(void *arg) {
    // cars move only if the light is green
    int result = 0; // if result = 1 : kraksa
    pid_t parentID = getppid();
    while(1){
        if(light){
            // move only if light is green
            result = moveCars(road);
            if(result == 1){
                // kraksa
                // stop everything
                //kill(parentID, SIGINT);
            }
        }
        sleep(1);
    }
}

void handleSignalUSR1(int s) {
    // creates new car at the end of the road
    // using signals one cant pass speed of a cor but using socket it's possible
    if (road[49] == 1){
        // crash sceanrio
        printf("Kiddo Uno: Crash");
        pid_t parentID = getppid();
        kill(parentID, SIGINT);
    }
    else{
        printf("Kiddo Uno: new car\n");
        road[49] = 1;
    }
}

void handleSignalUSR2(int s) {
    // creates new car at the end of the road
    // using signals one cant pass speed of a cor but using socket it's possible
    canChange = 1;
}



int main() {
    signal(SIGUSR1, handleSignalUSR1);
    signal(SIGUSR2, handleSignalUSR2);
    pid_t parentID = getppid();
    pid_t myID = getpid();

    // zmienna typu Id of thread
    pthread_t lightID;
    pthread_t roadID;

    // we should pass the int[50] road and bool light
    // tworzy thread z funkcji lightThread i przypisuje ID do lightID
    pthread_create(&lightID, NULL, lightThread, NULL);
    // tworzy thread z funkcji roadThread i przypisuje ID do roadID
    pthread_create(&roadID, NULL, roadThread, NULL);

    // czeka na zakoncznie threadID
    // pthread_join(threadID, NULL);
    while(1){
        //printf("Im kiddo Uno\n");
        printf("Uno: my ID: %d \n", myID);
        printf("Uno: light: %d\n", light);
        printf("Uno: road: [ ");
        for(int i = 0; i < roadLen; i++) {
            printf("%d ", road[i]);
        }
        printf("]\n");
        //printf("ID of my parent: %d \n", parentID);
        sleep(5);
    }

    return 0;
}