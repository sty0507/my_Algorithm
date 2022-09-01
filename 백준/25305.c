#include<stdio.h>
int arr[1000];
void swap(int a, int b){
	int temp = arr[a];
	arr[a] = arr[b];
	arr[b] = temp;
}
int partition(int left, int right){
	int pivot = arr[left], low = left+1, high = right, temp;
    while(low <= high) {
        while(low <= right && pivot >= arr[low]) low++;
        while(high >= (left+1) && pivot <= arr[high]) high--;
        if(low <= high) swap(low, high);
    }
    swap(left, high);
    return high;
}
void quickSort(int left, int right){
	if(left <= right) {
        int pivot = partition(left, right);
        quickSort(left, pivot-1);
        quickSort(pivot+1, right);
    }
}
int main(){
	int n, k; // n: 응시자 , k: 상 받는 수 
	int i;
	scanf("%d %d", &n, &k);
	for(i=0;i<n;i++){
		scanf("%d", &arr[i]);
	}
	quickSort(0, n-1);
	printf("%d", arr[n-k]);
	return 0;
}


