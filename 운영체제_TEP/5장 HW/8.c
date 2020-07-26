#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <sys/wait.h>

#define BUFF_SIZE 1024

int main(int argc, char *argv[])
{
    int pipes[2];
    char buff[BUFF_SIZE];
    int fd;

    pipe(pipes);

    int rc = fork();
    if (rc < 0)
    {
        printf("ERROR!\n");
    }
    else if (rc == 0)
    {
        close(pipes[0]);
        printf("STDOUT CHILD#1 (pid:%d) CLOSE STDOUT\n", (int)getpid());
        fflush(stdout);
        sprintf(buff, "자식 입력");
        dup2(pipes[1], 1);
        printf("%s\n", buff);
    }
    else
    {
        printf("PARENT (pid:%d)\n", (int)getpid());
        wait(NULL);
        int rc2 = fork();
        if (rc2 == 0)
        {
            close(pipes[1]);
            dup2(pipes[0], 0);
            printf("CHILD#2 (pid:%d) STDIN\n", (int)getpid());
            memset(buff, 0, BUFF_SIZE);
            read(STDIN_FILENO, buff, BUFF_SIZE);
            printf("%s\n", buff);
        }
    }

    return 0;
}