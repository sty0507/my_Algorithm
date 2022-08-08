#include<stdio.h>
int main(){
	int total, n, i, sum = 0;
	int cost, cnt;
	scanf("%d", &total);
	scanf("%d", &n);
	for(i=0;i<n;i++){
		scanf("%d %d", &cost, &cnt);
		sum += (cost * cnt);
	}
	if(sum == total) printf("Yes");
	else printf("No");
}
