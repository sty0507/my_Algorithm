#include<stdio.h>
#include<string.h>
int alpa[26];
char str[1000000];
void Search(char x){
	if(x < 91){//대문자인가 
		x = x + 32;
	}
	alpa[x - 97]++;
}
int maximum(){
	int i, max = 0, index = 0, result = 0;
	for(i =0; i<26; i++){
		if(alpa[i] > max){
			max = alpa[i];
			index = i;
		}
	}
	for(i =0; i<26; i++){
		if(i != index && alpa[i] == max){
			result = 1;
		}
	}
	if(result){
		return 0;
	}
	else
		return index + 65;
}
int main(){
	int i;
	scanf("%s", &str);
	int len = strlen(str);
	for(i=0;i<len;i++){
		Search(str[i]);
	}
	int res = maximum();
	if(res != 0){
		printf("%c", res);
	}
	else{
		printf("?");
	}
	return 0;
}
