#include<stdio.h>
int arr[10];
int Insert(int n){
	int i = 0;
	int x = 10;
	while(n != 0){
		arr[i] = n % x;
		i++;
		n = n /x;
	}
	return i;
}
void ShowInfo(int n){
	int i;
	for(i=0;i<n;i++){
		printf("%d", arr[i]);
	}
}
void Sort(int len){
	int i, j;
	int temp;
	for(i=0; i<len; i++){
		for(j=i+1; j<len; j++){
        	if(arr[i] < arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
		}
	}
}
int main(){
	int n;
	scanf("%d", &n);
	int len = Insert(n);
	Sort(len);
	ShowInfo(len);
	return 0;
}
