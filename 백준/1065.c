#include<stdio.h>
int one(int x){
	int i, cnt = 0;
	for(i=1; i<=x;i++){
		if(0<i && i<100){
			cnt++;
		}
		else{
			if((i / 100) - (i%100)/10 == (i%100)/10 - (i%100)%10){
				cnt++;
			}
		}
	}
	return cnt;
}
int main(){
	int n;
	scanf("%d", &n);
	printf("%d", one(n));
	return 0;
}
