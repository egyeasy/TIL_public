#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

#define BUFF_SIZE 1024

int main(int argc, char *argv[])
{
    char buff[BUFF_SIZE];
    int fd;
    //close(STDOUT_FILENO);
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
            x = 200;
            printf("PARENT (pid:%d) x: %d\n", (int)getpid(), x);
            read(fd, buff, BUFF_SIZE);
            puts(buff);
        }
        else if (rc == 0)
        {
            x = 150;
            printf("CHILD (pid:%d) x: %d\n", (int)getpid(), x);
            read(fd, buff, BUFF_SIZE);
            puts(buff);
            close(fd);
        }
    }

    return 0;
}