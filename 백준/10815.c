#include<stdio.h>
int arr[20000000];
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
		printf("%d ",Search(n, a));
	}
	return 0;
}
