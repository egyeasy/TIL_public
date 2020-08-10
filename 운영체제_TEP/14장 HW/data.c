#include <stdlib.h>
#include <stdio.h>

int main() {
  int* data = (int*) malloc(sizeof(int) * 100);
  //free(data);
  free(&data[20]);

  //*data = 0;
  //printf("%d\n", data[0]);

  return 0;
}
