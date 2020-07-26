#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <sys/wait.h>

#define BUFF_SIZE 1024

int main(int argc, char *argv[])
{
    char buff[BUFF_SIZE];
    int fd;
    if (0 < (fd = open("./2.output", O_CREAT | O_RDWR, S_IRWXU)))
    {
        int x = 100;
        // char *contents = "wow king";
        // write(fd, contents, strlen(contents));

        read(fd, buff, BUFF_SIZE);
        puts(buff);

        int rc = fork();
        if (rc > 0)
        {
            wait(NULL);
            x = 200;
            printf("PARENT (pid:%d) x: %d\n", (int)getpid(), x);
            // read(fd, buff, BUFF_SIZE);
            // puts(buff);
        }
        else if (rc == 0)
        {
            x = 150;
            printf("CHILD (pid:%d) x: %d\n", (int)getpid(), x);
            close(STDOUT_FILENO);
        }
    }

    return 0;
}