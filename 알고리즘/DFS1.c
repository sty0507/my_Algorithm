#include<stdio.h> 
#define MAX 1001
int adj[MAX][MAX]; //������� ���鶧 ��� 
int visited[MAX]; //�湮�ߴ��� check   
void init(int N) {
    for(int i=1; i<=N; i++) {
	    visited[i] = 0; //�湮�Ѱ� 0���� �ʱ�ȭ !    
	}
} 
// ��� ������Ʈ �湮
// void DFSAll(int N); 
void DFS(int here, int N) { //������ ��������
    int there;
	visited[here] = 1; //�湮 check
	printf("%d ", here); //���� ���
	for(int i = 1; i <= N; i++) {
	    if(adj[here][i]) {
		    there = i;
			if(!visited[there]) {
		        DFS(there, N); //�߰����ڸ��� �ٷ� �Լ��� �ٽ� ��
			}        
		}    
	}
} 
int main() {    
	int N,M,v; // ��������, ��������, ��������    
	int x,y; // ��ǥ        
	scanf("%d %d %d", &N, &M, &v);    
	for(int i=1; i<=M; i++) { //M(��������) ��ŭ
		scanf("%d %d", &x,&y);        
		adj[x][y]=1;        
		adj[y][x]=1; //������� �����    
	}        
	//DFS ȣ��    
	DFS(v, N);        
	return 0;
}

