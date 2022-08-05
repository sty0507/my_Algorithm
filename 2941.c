#include<stdio.h>
#include<string.h>
int main(){
	char str[100];
	int len, i, result;
	scanf("%s", str);
	len = strlen(str);
	result = len;
	for(i=0;i<len;i++){
		if(str[i+1] == '='){
			if(str[i] == 's' || str[i] == 'c' || str[i] == 'z'){
				result--;
			}
		}
		else if(str[i+1] == '-'){
			if(str[i] == 'd'){
				result--;
			}
			else if(str[i] == 'c'){
				result--;
			}
		}
		else if(str[i+1] == 'j'){
			if(str[i] == 'l' || str[i] == 'n'){
				result--;
			}
		}
		else if(str[i] == 'd'){
			if(str[i+1] == 'z' && str[i+2] == '='){
				result--;
			}
		}
	}
	printf("%d", result);
	
	return 0;
}
