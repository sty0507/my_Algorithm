#include<stdio.h>
int main(){
	int apt[15][15] = {0,};
	int t, k, n, i, j;
	scanf("%d", &t);
	for(i=0; i<15; i++){
		apt[0][i] = i;
	}	
	for(i=1;i<15;i++){
		for(j=1;j<15;j++){
			apt[i][j] = apt[i][j-1] + apt[i-1][j]; 
		}
	}
	for(i=0; i<t; i++){
		scanf("%d", &k);
		scanf("%d", &n);
		printf("%d\n", apt[k][n]);
	}
	
	return 0;
}
