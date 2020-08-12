#include <stdlib.h>

int main() {
  int* x = (int*) malloc(sizeof(int));
  *x = 23;

  return 0;
}
