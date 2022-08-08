#include <stdio.h>
#include <math.h>
#define size 10000
int num[size];
int insert(){//num배열에 인덱스가 소수인지 아닌지 (소수 1, 아니면 0) 
	int i, j, cnt;
	for(i=2; i<sqrt(size); i++){
		cnt = 0;
		for(j = 2; j<=i; j++){
			if(i %j == 0){
				cnt++;
			}
		}
		if(cnt == 1)
			num[i] = 1;
	} 
}
int main(){
	insert();
	int n, i, j, g;
	scanf("%d", &n);
	for(i = 0; i<n;i++){
		scanf("%d", &g);
		for(j = g / 2; j>0; j--){
			if(num[j] == 1 && num[g - j] == 1){
				printf("%d %d\n", j, g-j);
				break;
			}
		}
	}
	return 0;
}
