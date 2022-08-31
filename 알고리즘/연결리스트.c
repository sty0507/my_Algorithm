#include<stdio.h>
#include<stdlib.h>

typedef struct _Node {
	int data; // ��忡 ������ ������
    struct _Node * next // ���� ����� ���� ����� �ּҸ� ��� �ִ� ��, ���� ��� ������
}Node;
Node* head;
void init(){
    head = NULL;
}
void insert(int data){
    Node* ptr;
    Node* newNode = (Node*)malloc(sizeof(Node)); 
    newNode->data = data;    // ������ �Ҵ� 
    newNode->next = NULL;    // next ������ �ʱ�ȭ 
    
    if(head == NULL){    // empty
        head = newNode;
    }else{
		// not empty, ���� �տ� ��� �߰� 
        if(head->data > newNode->data){    
            newNode->next = head;
            head = newNode;
            return;
        }
		 // �߰��� ��� �߰� 
        for(ptr = head; ptr->next; ptr=ptr->next){   
            if(ptr->data < newNode->data && ptr->next->data > newNode->data){
                newNode->next = ptr->next;
                ptr->next = newNode;
                return;
            }
        }
        
        ptr->next = newNode;    // �������� ��� �߰�  
    }
    
}
int deleteNode(int data){
    Node *cur, *prev;
    cur = prev = head;
    
    if(head == NULL){    // empty list 
        printf("error: list is empty!\n");
        return -1;
    }        
    
    if(head->data == data){    // ���� ���� ��� ����
        head = cur->next;
        cur->next = NULL;
        free(cur);
        return 1;
    }
    
    for(; cur; cur= cur->next){    // �߰� Ȥ�� ������ ��� ����
        if(cur->data == data){
            prev->next = cur->next;
            cur->next = NULL;
            free(cur);
            return 1;
        }
        prev = cur;
    }
    
    printf("error : there is no %d!\n", data);
    return -1;    // �ش� �����Ͱ� ����Ʈ�� ����x
}
int search_list(int data){
    Node* ptr;
    for(ptr = head ; ptr ; ptr=ptr->next){
        if(ptr->data == data){    // data �߰�  
            return 1;
        }
    }
    
    return -1; // ������ �߰� x
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

