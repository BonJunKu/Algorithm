#include <iostream>
#include <queue>
#include <string>

#define MAX 51
using namespace std;


int r,c;
queue <pair<int,int>> q;
queue <pair<int,int>> water;
int x,y;
int s_x,s_y,e_x,e_y;
int nx, ny;
char graph[MAX][MAX];
int visit[MAX][MAX]={0,};

void init();
void BFS();
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};
int ans=-1;

int main(){
	init();
	//freopen("3055.txt","r",stdin);
	cin>>r>>c;
	//cout<<"r : "<<r<<" c : "<<c<<endl;
	
	//위치 기록은 물만 하면 됨. 바위는 탐색하면서 거른다  
	for (int i=0; i<r;i++){
		for (int j=0; j<c; j++){
			cin>>graph[i][j];
			if (graph[i][j]=='D'){
				e_x=i;
				e_y=j;
			}
			if (graph[i][j]=='S'){
				s_x=i;
				s_y=j;
			}
			if (graph[i][j]=='*'){
				water.push(make_pair(i,j));
			}
			
	
	}
}
	
	
	BFS();
	
//	for (int i=0; i<r; i++){
//		for (int j=0; j<c; j++){
//			
//			cout<<graph[i][j]<<" ";
//		}
//		cout<<endl;
//	}
	
	if(ans==-1) cout<<"KAKTUS";
	else cout<<ans;
	
}
	
void init(){
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
}
void BFS(){
	q.push(make_pair(s_x,s_y));
	visit[s_x][s_y]=1;
	int cnt=0;
	
	
	while (q.size()!=0){ 
		int water_size = water.size(); //water는 q가 빌때까지가 아니라 당시 크기만큼만 돌린다!!!! 뒤에 넣어주는 것은 고려X 
		while(water_size--){
		x=water.front().first;
		y=water.front().second;
		water.pop();
		
		for (int i=0; i<4; i++){
			nx=x+dx[i];
			ny=y+dy[i];
			if (nx<0 || ny<0 || nx>=r || ny>=c || graph[nx][ny] =='*' || graph[nx][ny] == 'D' ||graph[nx][ny]=='X'){
				continue;
			}
			else{
				graph[nx][ny]='*';
				water.push(make_pair(nx,ny));
			}
		}
			
		}
		
		int q_size = q.size();
		while(q_size--){
			x=q.front().first;
			y=q.front().second;
			q.pop();
			
			for (int i =0; i<4; i++){
				nx= x+dx[i];
				ny= y+dy[i];
				
				if (nx<0 || ny<0|| nx>=r || ny>=c|| graph[nx][ny] =='*' ||graph[nx][ny]=='X' ||visit[nx][ny] ==1){
					continue;
				}
				else if (graph[nx][ny]=='D'){
					
					ans=cnt+1;
					return; 
				}
				
				else {
					
					q.push(make_pair(nx,ny));
					visit[nx][ny]=1;
					
				}
			}
		}
		cnt++;
		
		
	}
}
