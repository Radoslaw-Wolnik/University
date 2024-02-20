#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t myID = getpid();
    const char *child = "./Z3kiddo";

    pid_t kiddoID = fork();

    if(kiddoID == -1){
      printf("something went wrong");
    }
    
    if(kiddoID == 0){
      printf("Starting kiddo");
      execlp(child, child,(char *)NULL);
    }
    else{
        int status;
        pid_t KiddoFinish = waitpid(kiddoID, &status, 0);
        //pid_t waitpid(pid_t kiddoID, int *status, int options);

        printf("Kiddo finished work");
        printf("My ID: %d \n", myID);

        return 0;
    }
    return 1;
}
