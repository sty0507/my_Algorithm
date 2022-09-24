#include<stdio.h>
#define max 100000
int dat[max];
int pos = 0;
void push(int x){
	dat[pos++] = x;
}
void pop(){
	pos--;
}
int top(){
	return dat[pos-1];
}
int Show(){
	int i = 0;
	while(i != pos){
		printf("%d ", dat[i]);
		i++;
	}
	printf("\n");
}
int main(){
	push(31);
	push(12);
	push(30);
	Show();
	push(10);
	Show();
	printf("%d\n", top());
	Show();
	pop();
	Show();
	return 0;
}
