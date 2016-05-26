#include "stdio.h"

float divide(int a, int b){
    return a / 0;
}

void main(){
  int n1 = 6;
  int n2 = 0;
  printf("%d / %d == %.2f", n1, n2, divide(n1, n2));
}
