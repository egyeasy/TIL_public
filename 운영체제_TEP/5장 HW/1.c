#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    int x = 100;
    int rc = fork();
    if (rc > 0)
    {
        x = 200;
        printf("PARENT (pid:%d) x: %d\n", (int)getpid(), x);
    }
    else if (rc == 0)
    {
        x = 150;
        printf("CHILD (pid:%d) x: %d\n", (int)getpid(), x);
    }
    return 0;
}