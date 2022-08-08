#include<stdio.h>
int arr[250000] = {0,};
int Fill(int n, int m){
	int i, j;
	arr[1] = 1;
	for(i=2; i<=m; i++){
		for(j=2;i*j<=m;j++){
			arr[i*j] = 1;// 0이여야 소수 
		}
	}
	return;
}
int Search(int n, int m){
	int i;
	int result = 0;
	for(i=n+1;i<=m;i++){
		if(arr[i] == 0)
			result++;
	}
	return result;
}
//int Show(int m){
//	int i;
//	for(i=0; i<m; i++){
//		printf("%d\n", arr[i]);
//	}
//}
int main(){
	int n;
	while(1){
		scanf("%d", &n);
		if(n == 0)
			break;
		Fill(n, 2*n);
//		Show(2*n);
		printf("%d\n", Search(n, 2*n));
	}
	return 0;
}
