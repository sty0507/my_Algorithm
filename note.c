#include<stdio.h>
#define SWAP(x,y,temp) ((temp) = (x), (x)=(y), (y)=(temp))
#define MAX_SIZE 50
// A배열은 오름차순
// B배열은 내림차순 

// 문제해결 방법
// A배열의 제일 작은 수와 B 배열의 제일 큰 수를 곱한다.
// 그렇게 하나씩 내려오면서 곱하고 그 값을 더한다.

//사용 알고리즘
// quick_sort(퀵 정렬) 

//----------------퀵정렬--------------------------------
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
	//------배열 입력----
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
