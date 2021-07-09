//N:사진틀 수  [1,20]
//recommend: 추천 수 [1,1000]
//학생수:1~100 
//일단 배열에 저장을 하고,  
//벡터의 초기화 방법 중 v(개수, 원소) 도 있음
//추천수, 추천을 받은 시점, 사용된 사진틀 수를 따로 카운트
//when은 최초등록시만 등록이 되고, 삭제시에 초기화된다. 

#include <iostream>
#include <vector>
using namespace std;

int n,k;
int rec[101]={0,};
int when[101]={0,};
int used;

int main(){
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	//freopen("1713.txt","r",stdin);
	cin>>n>>k;
	int student;
	for (int i=1; i<=k; ++i){
		cin>>student;
		if (rec[student]!=0){
			rec[student]++;
		}
		else{
			if (used<n){
				rec[student]++;
				used++;
				when[student]=i;
			}
			else{
				int max=9999;
				int exchangable;
				for (int j=1; j<=100;++j){
					if (rec[j]==0){
						continue;
					}
					else if (max>rec[j]){
						max=rec[j];
						
						exchangable=j;
					}
					else if (max==rec[j]){
						if (when[j]<when[exchangable]){
							exchangable=j;
						}
					}
				}
				rec[student]++;
					when[student]=i;
					rec[exchangable]=0;
					when[exchangable]=0;
			}
		}
		

	}
	for (int i=1; i<=100; ++i){
		if (when[i]!=0) cout<< i <<' ';
	}
	
	
	
	
	return 0;
} 
