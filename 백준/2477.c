#include<stdio.h>
int arr[4];
int direction[2][4];
int main(){
	int n, sum = 0, j;
	int dir, dis;
	int h=0, w=0,h1=0, w1=0;
	scanf("%d", &n);
	for(int i=0;i<6;i++){
		j = 0;
		scanf("%d %d", &dir, &dis);
		if(arr[dir-1] == 1){
			j++;
			direction[dir-1][j] = dis;
		}
		arr[dir-1] ++;
	}
	for(int i=0;i<4;i++){
		for(int j=0;j<arr[i];j++){
			if(i == 0 || i == 1){
				h += arr[i][j];
			}
			else{
				w += arr[i][j];
			}
		}
	}
}

