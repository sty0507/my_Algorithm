#include <stdio.h>
int list[1001];


int sort(int n){
    int i, j, key;
    for(i=0; i<n;i++){
        key = list[i];
        for(j=i-1; j>=0 && list[j] > key; j--) list[j+1] = list[j];
        list[j+1] = key;
    }
    return 0;
}
int Show(int n){
    int sum = 0;
    for(int i=0; i<n; i++){
        for(int j=i; j>=0; j--){
            sum += list[j];
        }
    }
    printf("%d", sum);
    return 0;
}

// 큰 수가 뒤로 갈 수록 합이 작아짐
int main(){
    int n;
    scanf("%d", &n);
    for(int i=0;i<n;i++){
        scanf("%d", &list[i]);
    }   
    sort(n);
    Show(n);
    return 0;
}
