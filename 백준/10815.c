#include<stdio.h>
int arr[20000000];
int result[500000];
int Search(int m, int a){
	int i;
	for(i=0;i<m;i++){
		if(arr[i] == a){
			return 1;
		}
	}
	return 0;
}
int main(){
	int n, m, i, a;
	scanf("%d", &n);
	for(i=0;i<n;i++){
		scanf("%d", &arr[i]);
	}
	scanf("%d", &m);
	for(i=0;i<m;i++){
		scanf("%d", &a);
		result[i] = Search(n, a);
	}
	for(i=0;i<m;i++){
		printf("%d ", result[i]);
	}
	return 0;
}
