//K:����ĥ ���� ��
//N:�� �ܾ� �� <=50
//���ܾ� ����: 8~15
//�ܾ ��Ʈ����ũ�� ���� �迭 word[50] 
//���ĺ��� 4����Ʈ �ȿ� ��Ʈ�������� ������ ����(26�ڸ�) 
//learn�� acint ����
//���ڿ��� �Է¹ް�, �� ���ڿ��� �ѱ��ھ� ��Ʈ����ŷ������� word�� ����
//K�� 5���� ������ �ϳ��� �����.
//K�� 26�̸� N�� ����.
//�ƴϸ� DFS
//DFS�� ��� combination�� ����� �����ϴ�. ���� ������ ��� �޶���.
//max���� ���� ����� ����. 
// word[i]�ش� �ܾ�� learned�� ���� �� '������' ī��Ʈ�ϴ� ���� �ƴ϶�
// and ������ �����ص� word�� ��Ʈ���� ������ ������! ī��Ʈ�Ѵ�.  
 
 

#include <iostream>
#include <string>
#include <bitset>
using namespace std;



int n,k;
int word[50];
int learned;
int res;
int cnt;
int max(int a, int b){
	if (a>=b){
		return a;
	}
	else {
	return b;}
}
void dfs(int start, int learning){
	
	if (learning == k){
		for (int i=0; i<n; i++){
			if ((word[i]&learned)==word[i]){
				cnt++;
			}
		}
		
		res=max(res,cnt);
		cnt=0;
		return;
		
	}
	
	for (int k=start; k<26; k++){
		
		if ((learned&(1<<k))==0){
			
			learned|=1<<k;
			
			dfs(k+1,learning+1);
			learned&=~(1<<k);
		}
		
	}
	
	
};


int main(){
	freopen("1062.txt","r",stdin);
	cin>>n>>k;
	if (k<5){
		cout<<0;
		return 0;
	}
	else if (k==26){
		cout<<n;
		return 0;
	}
	
	for (int i=0; i<n; i++){
		
		string str;
		cin>>str;
		for (int j=0; j<str.size();j++){
			word[i]|=1<<str[j]-'a';
				
		}	
	}
	learned|=1<<('a'-'a');
	learned|=1<<('c'-'a');
	learned|=1<<('i'-'a');
	learned|=1<<('n'-'a');
	learned|=1<<('t'-'a');
	
	dfs(0,5);
	
	
	
	cout<<res<<endl;
	
	return 0;
}
