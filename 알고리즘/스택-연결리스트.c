#include<stdio.h>
typedef struct stack{ // ���� ����Ʈ ��� ����ü ���� 
	char data; // data�� ������ ���� 
	struct stack* link; // ���� ����� �ּҰ�(���� ��带 ����Ű��)�� ������ ������ ���� 
}stack;
stack * top;//������ ���� 

int IsEmpty(){//������ ���� �������� �˻��ϴ� �Լ� 
	if(top == NULL){//top�� NULL�� ��� 
		printf("Error : Stack is Empty. \n");
		return 1;//true 
	}
	return 0;//false 
}
void push(char data){//������ ��忡 �����ϴ� �Լ� 
	stack* newnode = (stack *)malloc(sizeof(stack));//���ο� ��� newnode �����Ҵ� 
	newnode -> data = data;//newnode�� data�� �� ���� 
	newnode -> link = top;//newnode�� link�� �� ���� ��� �ּ� ����(top�� �� ���� ��� �ּҸ� ������ ����) 
	top = newnode;//top�� newnode�� �ּ� ���� 
}
char pop(){// ���ÿ� ��带 �����ϴ� �Լ� 
	if(!IsEmpty()){//�迭�� ������� ���� ��� 
		stack* temp = top;//temp ������ ������ ������ �� �� ����� �ּҰ��� ���� 
		char data = temp -> data;//data ������ ���� �����Ͽ� �� �� ����� ������ ���� 
		top = temp -> link;//top �����Ϳ� 2��° ���(�� �� ���� ���)�� �ּҰ� ���� 
		free(temp);//�� �� ��� ���� 
		return data;//������ ��ȯ 
	}
}
char peek(){//������ �� ���� ���Ҹ� ��ȯ�ϴ� �Լ� 
	if(!IsEmpty()){//������ ��� ���� ���� ��� 
		return top ->data;//�� �� ����� ������ ��ȯ 
	}
}
void ShowStack(){//������ ����ϴ� �Լ� 
	if(!IsEmpty()){//������ ������� ���� ��� 
		stack * temp = top;//�� ������ �����ϱ� ���� temp ���� ���� 
		while(temp){//���� ��尡 NULL�� �ƴ� ��� �ݺ� 
			printf("%c ", temp -> data);//���� ����Ű�� ����� data ��� 
			temp = temp -> link;//temp�� ���� ��带 ����Ű���� �� 
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
