#include <stdio.h>
int countf = 0;
int countfib = 0;
int f[40];
int fib(int n){

    if (n == 1 || n == 2)
        return 1;
    else
        countf++;
        return (fib(n-1)+fib(n-2));
}

int fibonacci(int n){
    
    f[0], f[1] = 1;
    for(int i=2; i<n; i++){
        f[i] = f[i-1] + f[-2];
        countfib++;
    }
    return f[n];
}

int main(){
    int n;
    scanf("%d", &n);
    fib(n);
    fibonacci(n);
    printf("%d %d", countf+1, countfib);
    return 0;
}
