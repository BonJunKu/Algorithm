//N:����Ʋ ��  [1,20]
//recommend: ��õ �� [1,1000]
//�л���:1~100 
//�ϴ� �迭�� ������ �ϰ�,  
//������ �ʱ�ȭ ��� �� v(����, ����) �� ����
//��õ��, ��õ�� ���� ����, ���� ����Ʋ ���� ���� ī��Ʈ
//when�� ���ʵ�Ͻø� ����� �ǰ�, �����ÿ� �ʱ�ȭ�ȴ�. 

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
