#include <stdio.h>
int n;
const char *str[7] = {
    "\"재귀함수가 뭔가요?\"\n",
    "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n",
    "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n",
    "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n",
    "\"재귀함수가 뭔가요?\"\n",
    "\"재귀함수는 자기 자신을 호출하는 함수라네\"\n",
    "라고 답변하였지.\n"
};
void explain(int a){
	int i, j;
	for(i = 0; i<4; i++){
		for(j = 1; j<a;j++) printf("____");
		printf(str[i]);
	}
	if(n != a) explain(a+1);
	else{
		for(i = 4; i<7;i++){
			for(j=0;j<a;j++) printf("____");
			printf(str[i]);
		}
	}
	for(j = 1; j<a;j++) printf("____");
	printf(str[6]);
}
int main(){
	scanf("%d", &n);
	printf("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n");
	explain(1);
}
