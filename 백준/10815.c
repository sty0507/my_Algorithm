#include<stdio.h>
#include<stdlib.h>
int arr[20000000];
void Search(int a, int n){
	int i;
	for(i=0;i<n;i++){
		if(arr[i] == a){
			printf("1 ");
			return;
		}
	}
	printf("0 ");
	return;
}
int compare(const int *a, const int *b){
	if(*a < *b)
		return -1;
	else if(*a>*b)
		return 1;
	else return 0;
}
int main(){
	int n,m,i,a;
	scanf("%d", &n);
	for(i=0;i<n;i++){
		scanf("%d", &arr[i]);
	}
	qsort(arr, n, sizeof(int), compare);
	scanf("%d", &m);
	for(i=0;i<m;i++){
		scanf("%d", &a);
		Search(a,n);
	}
	return 0;
}

