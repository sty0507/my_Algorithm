#include<stdio.h>
int SequentialSearch(int data[], int len, int find){
	for(int i=0;i<len;i++){
		if(data[i] == find) return i;
	}
	return -1;
}
int main(){
	int arr[]={1,4,5,3};
	int len = sizeof arr/sizeof arr[0];
	int find = 5; // 찾으려는 데이터
	int index;
	while(1){
		index = SequentialSearch(arr, len, find);
		if(index == -1)
			printf("Nope");
		else{
			printf("You cna find at %d.", index);
			break;
		}
	}
	return 0;
}
