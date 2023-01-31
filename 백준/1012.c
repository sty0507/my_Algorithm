#include<stdio.h>
int a[50][50];
int cnt;
int m, n, k, t; 
// m : 가로 길이, n : 세로 길이 
// t : 데스트 케이스 수, k : 배추의 위치
int dfs(int x, int y){
	a[x][y] = 0;
	
	if(a[x+1][y] == 1 && x+1 < m) dfs(x+1, y);
	if(a[x-1][y] == 1 && x-1 >= 0) dfs(x-1, y);
	if(a[x][y+1] == 1 && y+1 <n) dfs(x, y+1);
	if(a[x][y-1] == 1 && y-1 >= 0) dfs(x, y-1);
	
	return 0;
}
int main(){
	int x, y; 
	scanf("%d", &t);
	for(int test=0; test<t; test++){
		scanf("%d %d %d", &m,&n,&k);
		for(int i=0;i<k;i++){
			scanf("%d %d", &x, &y);
			a[x][y] = 1;
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(a[j][i] == 1){
					dfs(j,i);
					cnt++;
				}
			}
		}
		printf("%d\n" , cnt);
		cnt = 0;
	}
	return 0;
	
}
