//K:가르칠 글자 수
//N:총 단어 수 <=50
//영단어 길이: 8~15
//단어가 비트마스크로 담기는 배열 word[50] 
//알파벳은 4바이트 안에 비트형식으로 저장이 가능(26자리) 
//learn에 acint 저장
//문자열을 입력받고, 그 문자열의 한글자씩 비트마스킹방식으로 word에 저장
//K가 5보다 작으면 하나도 못배움.
//K가 26이면 N이 나감.
//아니면 DFS
//DFS의 경우 combination과 기능이 유사하다. 시작 범위가 계속 달라짐.
//max값을 최종 결과로 수정. 
// word[i]해당 단어와 learned를 비교할 때 '같으면' 카운트하는 것이 아니라
// and 연산을 수행해도 word의 비트들이 꺼지지 않으면! 카운트한다.  
 
 

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
