#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdbool.h>

bool flag = 1;

void handleSignalINT(int s) {
  if (flag){
    fprintf(stdout, "Jestem niesmiertelny!\n");
    // Different way of writing to terminal - using descriptor 1 : stdout
    dprintf(1, "Descriptor 1\n");
    // and this doesnt work idk why :(
    //fprintf(STDOUT_FILENO, "fileno\n", 5);
  }
}

void handleSignalHUP(int s){
  flag = 0;
}

int main() {
  signal(SIGINT, handleSignalINT);
  signal(SIGHUP, handleSignalHUP);

  while(1){
    sleep(1);
  }

  return 0;
}