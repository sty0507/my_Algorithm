#include<stdio.h>
int a[1000000];
int main(){
	int n, b, c;//b:총감독관,c:부감독관 
	int i, tmp, tmp1, tmp2;
	scanf("%d", &n);
	for(i=0;i<n;i++){
		scanf("%d", &a[i]);
	}
	scanf("%d %d", &b, &c);
	long long sum = 0;	
	sum = n;
	for(i=0;i<n;i++){
		tmp = a[i] - b;
		if(tmp > 0){
			tmp1 = tmp/c;
			tmp2 = tmp%c;
			if(tmp2 > 0){
				tmp2 = 1;
			}
			sum += tmp1 + tmp2;
		}
	}
	
	printf("%lld", sum);
	
	return 0;
}
