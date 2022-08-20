#include<stdio.h>
int forbinarySearch(int arr[], int low, int high, int key){
	while(low <= high){
		int mid = low + (high - low)/2;
		if(arr[mid] == key)
			return mid;
		else if(arr[mid] > key)
			high = mid - 1;
		else
			low = mid + 1;
	}
	return -1;
}
int binarySearch(int arr[], int low, int high, int key){
	if(low > high)
		return -1;
	int mid = low + (high-low)/2;
	if(arr[mid] == key)
		return mid;
	else if(arr[mid] > key)
		return binarySearch(arr, low, mid-1, key);
	else
		return binarySearch(arr, mid+1, high, key);
}
int main(){
	int arr[] = {1,2,3,4,5};
	int len = sizeof arr/sizeof int;
	int k = 4;//ã�� ��
	forbinarySearch(arr, 0, len, k);//�ݺ����� �̿��� ���� Ž�� 
	binarySearch(arr, 0, len, k);//����Լ��� �̿��� ���� Ž�� 
}
