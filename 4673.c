#include<stdio.h>
int arr[10001];
int self_num(int number){
	int sum = number;
	while(number != 0){
		sum = sum + (number % 10);
		number = number / 10;
	}
	return sum;
}
int main(){
	int i, n= 0;
	for(i = 1; i < 10001; i++){
		n = self_num(i);
		arr[n] = 1;
	}
	for(i = 1; i<10001; i++){
		if(arr[i] != 1)
			printf("%d\n", i);
	}
	return 0;
}
