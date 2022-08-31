#include<stdio.h>
#include<string.h>
struct who{
	char name[21];
}who;

struct who l[500000];
struct who s[500000];
int a[500000];
int check(char name[21], char name1[21]){
	int ret =0;
	ret = strcmp(name, name1);
	return ret;
}
int Search(char name[21], int n){
	for(int i=0;i<n;i++){
		if(name == s[i].name == 0){
			return 1;
		}
	}
	return 0;
}
int main(){
	int n, m;
	scanf("%d %d", &n, &m);
	for(int i=0;i<n;i++){
		scanf("%s", l[i].name);
	}
	for(int i=0;i<m;i++){
		scanf("%s", s[i].name);
	}
	for(int i=0;i<n;i++){
		if(Search(l[i].name, m) == 1){
			a[i]++;
		}
	}
	for(int i=0;i<n+m;i++){
		printf("%d", a[i]);
	}
}
