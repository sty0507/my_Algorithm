#include<stdio.h>
typedef struct stack{ // 연결 리스트 노드 구조체 정의 
	char data; // data를 저장할 변수 
	struct stack* link; // 다음 노드의 주소값(다음 노드를 가리키는)을 저장할 포인터 변수 
}stack;
stack * top;//스택의 맨위 

int IsEmpty(){//스택이 공백 상태인지 검사하는 함수 
	if(top == NULL){//top이 NULL인 경우 
		printf("Error : Stack is Empty. \n");
		return 1;//true 
	}
	return 0;//false 
}
void push(char data){//스택을 노드에 삽입하는 함수 
	stack* newnode = (stack *)malloc(sizeof(stack));//새로운 노드 newnode 동적할당 
	newnode -> data = data;//newnode의 data에 값 저장 
	newnode -> link = top;//newnode의 link에 맨 위의 노드 주소 저장(top이 맨 위에 노드 주소를 가지고 있음) 
	top = newnode;//top에 newnode의 주소 저장 
}
char pop(){// 스택에 노드를 제거하는 함수 
	if(!IsEmpty()){//배열이 비어있지 않은 경우 
		stack* temp = top;//temp 포인터 변수를 선언해 맨 위 노드의 주소값을 저장 
		char data = temp -> data;//data 변수를 새로 선언하여 맨 위 노드의 데이터 저장 
		top = temp -> link;//top 포인터에 2번째 노드(맨 위 다음 노드)의 주소값 저장 
		free(temp);//맨 위 노드 제거 
		return data;//데이터 반환 
	}
}
char peek(){//스택의 맨 위의 원소를 반환하는 함수 
	if(!IsEmpty()){//스택이 비어 있지 않은 경우 
		return top ->data;//맨 위 노드의 데이터 반환 
	}
}
void ShowStack(){//스택을 출력하는 함수 
	if(!IsEmpty()){//스택이 비어있지 않은 경우 
		stack * temp = top;//각 노드들을 접근하기 위한 temp 변수 선언 
		while(temp){//현재 노드가 NULL이 아닐 경우 반복 
			printf("%c ", temp -> data);//현재 가리키는 노드의 data 출력 
			temp = temp -> link;//temp가 다음 노드를 가리키도록 함 
		}
		printf("\n");
	}
}
int main(){
	ShowStack();
	push('A');
	push('B');
	push('C');
	ShowStack();
	pop();
	ShowStack();
	push('D');
	push('E');
	push('F');
	ShowStack();
	pop();
	pop();
	ShowStack();
	return 0;
}
