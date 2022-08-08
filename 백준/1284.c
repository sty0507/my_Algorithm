#include<stdio.h>

int renum(int num){
	switch(num){
		case 1:
			return 2;
			break;
		case 0:
			return 4;
			break;
		default:
			return 3;
			break;
	}
}
int main(){
	int n, sum = 2 , t = 10;
	do{
		sum = 2;
		scanf("%d", &n);
		if(n == 0)
			break;
		while(n != 0){
			sum += renum(n % t)+1;
			n = n / t;

		}
		printf("%d\n", sum-1);
	}while(1);
	return 0;
}

