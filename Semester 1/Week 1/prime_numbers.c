#include <stdio.h>
#include <time.h>

int prime(int n){
    int j;
    for (j=2;j<=n/2;j++)
        if((n%j)==0)
            return 0;
   return 1;
}

void main(){
    clock_t begin, end;
    double time_spent;
    int n = 20000;
    begin = clock();
    int i,p;
    for (i=2;i<=n;i++){
        p=prime(i);
        if(p==1){
            printf("%d \n",i);
        }
    }

    end = clock();
    time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%g seconds", time_spent);
}
