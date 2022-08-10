#include<stdio.h>
int arr[100];

int ShowInfo(){
	int i;
	for(i=0; i<n; i++) printf("%d ", arr[i]);
}
//���� ����(Sequential Sort)
int Sequential(){
	int n, temp;
	int i, j;
	scanf("%d", &n);
	for(i=0;i<n;i++) scanf("%d", &arr[i]);
	for(i=0; i<n; i++){
		for(j=i+1; j<n; j++){
        	if(arr[i] > arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
		}
	}
            
    ShowInfo();
}
//

//���� ����(Bubble Sort)
int Bubble(){
	int n, i, temp, j;
	scanf("%d", &n);
	for(i=0;i<n;i++) scanf("%d",&arr[i]);
	for(i=0; i<n-1; i++)
	{
		for(j=0; j<n-1-i; j++){
        	if(arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
		}
	} 

    ShowInfo();
}
//

//���� ����(Insertion Sort)
int Insertion(){
	int n, i, temp, j;
	scanf("%d", &n);
    for(i=0; i<n; i++) scanf("%d", &arr[i]);

    for(i=1; i<n; i++) {
        temp = arr[i];
        for(j=i; j>0 && arr[j-1]>temp; j--) arr[j] = arr[j-1];
        arr[j] = temp;
    }

   	ShowInfo();
}
// 

// ���� ����(Selection Sort)
int Selection(){
	int n, i, temp, j;
	scanf("%d", &n);
    for(int i=0; i<n; i++) scanf("%d", &arr[i]);

    int min;
    for(int i=0; i<n; i++) {
        min = i;
        for(int j=i; j<n; j++) if(arr[j] < arr[min]) min = j;
        temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
    ShowInfo();
}
//

//���� ����(Merge Sort)
void merge(int left, int mid, int right){
	int arrCopy[100], i = left; j = mid + 1, k=left, a;
	while(i<=mid && j<=right){
		if(arr[i] <= arr[j]) arrCopy[k++] = arr[i++];
		else arrCopy[k+=] = arr[j++];
	}
	while(i<=mid) arrCopy[k++] = arr[i++];
    while(j<=right) arrCopy[k++] = arr[j++];
    for(a=left; a<=right; a++) arr[a] = arrCopy[a];
}
void mergeSort(int left, int right) {
    int mid;
    if(left < right) {
        mid = (left+right)/2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid+1, right);
        merge(arr, left, mid, right);
    }
}
int mergeMain(){
	int n, i;
	scanf("%d", &n);
	for(i=0;i<n;i++) scanf("%d", &arr[i]);
	mergeSort(0, n-1);
	ShowInfo();
}
// 

//�� ����(Quick Sort)
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
        if(low <= high) swap(arr, low, high);
    }
    swap(arr, left, high);
    return high;
}
void quickSort(int left, int right){
	if(left <= right) {
        int pivot = partition(arr, left, right);
        quickSort(arr, left, pivot-1);
        quickSort(arr, pivot+1, right);
    }
}
int quickMain(){
	int n, i;
	scanf("%d", &n);
	for(i=0;i<n;i++) scanf("%d", &arr[i]);
	quickSort(0, n-1);
	ShowInfo();
}
// 
int Reset(){
	int i;
	for(i=0;i<100;i++){
		arr[i] = 0;
	}
}
int main(){
	Sequential();//���� ����
	Reset();
	Bubble();//���� ���� 
	Reset();
	Insertion();//���� ���� 
	Reset();
	Selection();//���� ���� 
	Reset();
	mergeMain();//���� ����
	Reset(); 
	quickMain();//�� ���� 
	return 0;
}

//���� :  https:restudycafe.tistory.com/319
