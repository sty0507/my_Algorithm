#include<stdio.h>
#define SWAP(x,y,temp) ((temp) = (x), (x)=(y), (y)=(temp))
#define MAX_SIZE 50
// A�迭�� ��������
// B�迭�� �������� 

// �����ذ� ���
// A�迭�� ���� ���� ���� B �迭�� ���� ū ���� ���Ѵ�.
// �׷��� �ϳ��� �������鼭 ���ϰ� �� ���� ���Ѵ�.

//��� �˰���
// quick_sort(�� ����) 

//----------------������--------------------------------
int partition(int list[], int left, int right){
	int pivot, temp;
	int low, high;
	
	low = left;
	high = right + 1;
	pivot = list[left];
	
	do{
		do{
			low++;
		}while(low<=right && list[low] < pivot);
		
		do{
			high--;
		}while(high >= left && list[high] > pivot);
		
		if(low<high){
			SWAP(list[low],list[high], temp);
		}
	}while(low<high);
	SWAP(list[left], list[high], temp);
	return high;
}

void quick_sort(int list[], int left, int right){
	if(left<right){
		int q = partition(list, left, right);
		
		quick_sort(list, left, q-1);
		quick_sort(list, q+1, right);
	}
}
//---------------------------------------------------

int main(){
	int n, i;
	int A[MAX_SIZE], B[MAX_SIZE];
	scanf("%d", &n);
	//------�迭 �Է�----
	for(i = 0; i<n;i++){
		scanf("%d", &A[i]);
	}
	for(i = 0; i<n;i++){
		scanf("%d", &B[i]);
	}
	//---------------
	quick_sort(A, 0, n-1);
	quick_sort(B, 0, n-1);
	int j = n-1, sum = 0;
	for(i = 0; i<n; i++){
		sum += A[i] * B[j];
		j--;
	}
	printf("%d", sum);
	
}
