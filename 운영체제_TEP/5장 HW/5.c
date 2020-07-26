#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    int x = 100;
    int rc = fork();
    if (rc > 0)
    {
        int wrc = wait(NULL);
        printf("PARENT (pid:%d) x: %d, wait: %d\n", (int)getpid(), x, wrc);
    }
    else if (rc == 0)
    {
        int wrc = wait(NULL);
        x = 150;
        printf("CHILD (pid:%d) x: %d, wait: %d\n", (int)getpid(), x, wrc);
    }
    return 0;
}