#include<stdio.h>
#include<stdlib.h>
int arr[30000];
int main(){
	int i = 2, result = 2, n = 0, max=0, k=0;
	int max_arr;
	scanf("%d", &n);
	arr[0] = n;
	for(k=1;k<n;k++){
		arr[1] = k;
		while(1){
			if(arr[i] < 0)
				break;
			arr[i] = arr[i-2] - arr[i-1];
			i++;
			result++;
		}
		if(result > max){
			max = result;
			max_arr = k;
		}
		i = 2;
		result = 2;
	}
	arr[1] = max_arr;
	i = 2;
	while(1){
		if(arr[i] <0)
			break;
		arr[i] = arr[i-2] - arr[i-1];
		i++;
	}
	printf("%d", max);
	for(i=0;arr[i] != 0; i++){
		printf("%d ", arr[i]);
	}
	
	return 0;
}
