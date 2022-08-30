#include<stdio.h>
int arr[100];
int main(){
	int n;
	int cnt=0, result =0;
	scanf("%d", &n);
	for(int i=0;i<n;i++){
		scanf("%d", &arr[i]);
	}
	for(int i=0;i<n;i++){
		if(arr[i] == 1){
			cnt++;
			if(cnt > 1)
				result += cnt;
			else
				result++;
		}
		else{
			cnt = 0;
		}
	}
	printf("%d", result);
	return 0;
}
