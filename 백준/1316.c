#include<stdio.h>
#include<string.h>
int main(){
	int n, i, j;
	int result, len = 0;
	char str[100];
	scanf("%d", &n);
	result = n;
	for(i=0;i<n;i++){
		int alpa[26] ={0,};
		scanf("%s", str);
		len = strlen(str);
		for(j=0;j<len;j++){
			alpa[str[j] - 'a']++;
			if(str[j] != str[j-1] && alpa[str[j] -'a'] > 1){
				result--;
				break;
			}
		}
	}
	printf("%d", result);
	
	return 0;
}
