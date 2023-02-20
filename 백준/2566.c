#include <stdio.h>
int arr[9][9];
int main(){
    int max = 0;
    int max_i, max_j;
    int i,j,k;
    for(i = 0; i<9; i++){
        for(j = 0; j<9; j++){
            scanf("%d", &arr[i][j]);
            if(arr[i][j] >= max){
                max = arr[i][j];
                max_i = i + 1;
                max_j = j + 1;
            }
        }
    }

    printf("%d\n", max);
    printf("%d %d", max_i, max_j);

    return 0;
}