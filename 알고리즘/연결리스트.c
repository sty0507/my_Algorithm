#include<stdio.h>
#include<stdlib.h>

typedef struct _Node {
	int data; // 노드에 저장할 데이터
    struct _Node * next // 현재 노드의 다음 노드의 주소를 담고 있는 곳, 다음 노드 포인터
}Node;
Node* head;
void init(){
    head = NULL;
}
void insert(int data){
    Node* ptr;
    Node* newNode = (Node*)malloc(sizeof(Node)); 
    newNode->data = data;    // 데이터 할당 
    newNode->next = NULL;    // next 포인터 초기화 
    
    if(head == NULL){    // empty
        head = newNode;
    }else{
		// not empty, 가장 앞에 노드 추가 
        if(head->data > newNode->data){    
            newNode->next = head;
            head = newNode;
            return;
        }
		 // 중간에 노드 추가 
        for(ptr = head; ptr->next; ptr=ptr->next){   
            if(ptr->data < newNode->data && ptr->next->data > newNode->data){
                newNode->next = ptr->next;
                ptr->next = newNode;
                return;
            }
        }
        
        ptr->next = newNode;    // 마지막에 노드 추가  
    }
    
}
int deleteNode(int data){
    Node *cur, *prev;
    cur = prev = head;
    
    if(head == NULL){    // empty list 
        printf("error: list is empty!\n");
        return -1;
    }        
    
    if(head->data == data){    // 가장 앞의 노드 삭제
        head = cur->next;
        cur->next = NULL;
        free(cur);
        return 1;
    }
    
    for(; cur; cur= cur->next){    // 중간 혹은 마지막 노드 삭제
        if(cur->data == data){
            prev->next = cur->next;
            cur->next = NULL;
            free(cur);
            return 1;
        }
        prev = cur;
    }
    
    printf("error : there is no %d!\n", data);
    return -1;    // 해당 데이터가 리스트에 존재x
}
int search_list(int data){
    Node* ptr;
    for(ptr = head ; ptr ; ptr=ptr->next){
        if(ptr->data == data){    // data 발견  
            return 1;
        }
    }
    
    return -1; // 데이터 발견 x
}
void printList(){
    Node* ptr;
    for(ptr=head; ptr->next; ptr= ptr->next){
        printf("%d->", ptr->data);
    }
    printf("%d\n", ptr->data);
}
int main(){
    int data;
    
    init();
    insert(100);
    insert(300);
    insert(50);
    insert(200);
    printList();
    deleteNode(50);
    printList();
    deleteNode(200);
    printList();
         
    return 0;
}

