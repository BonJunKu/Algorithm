#include <cstdio>
//명령 번호 
//NUMX : 0
//POP : 1
//INV : 2
//DUP : 3
//SWP : 4
//ADD : 5
//SUB : 6
//MUL : 7
//DIV : 8
//MOD : 9

//스택의 크기 : 1000개 이상이 넘어가는 경우 없으므로 0~1000
//스택의 범위:  10억을 넘기면 에러이므로 int로 커버 가능
//명령의 개수 = 최대 100000개
//프로그램 수행횟수: 최대 10000번

//입력 구조가 커맨드가 쭉 나오고 값이 주어지는 형식이기 때문에, 
//명령 자체도 배열에 담아서 보관해야 함. 명령의 최대 개수 = 10^5 
 


int flag;
char line[5];
int stack[10001];
int command[100001];

void program();
void input();

void numx();
void pop();
void inv();
void dup();
void swp();
void add();
void sub();
void mul();
void div();
void mod(); 


int main(){
	freopen("input.txt","r",stdin);
	for(;;){
	
	program();
	input();
	
	
	if (flag==-1){
		break;
	}
}
return 0;	
}
void program(){
	for(;;){
		
		scanf("%s",line);
		printf("%s\n",line);
		
		if (line[0]=='N'){
		numx();
		}
		if (line[0]=='P'){
		pop();
		}
		if (line[0]=='I'){
		inv();
		}
		if (line[0]=='D'){
		if (line[1]=='U'){
		dup();
		}
		else{
		div();
		}
		}
		if (line[0]=='S'){
		if (line[1]=='W'){
			swp();
		}
		else{
		sub();
		}
		}
		
		if (line[0]=='M'){
		if (line[1]=='U'){
		mul();}
		else{
		mod();
		}
		}
	
		if (line[0]=='E'){
		break;
		}
		
		if (line[0]=='Q'){
		flag=-1;
		break;
		}
	}
};

void input(){
	
}
void numx(){};
void pop(){};
void inv(){};
void dup(){};
void swp(){};
void add(){};
void sub(){};
void mul(){};
void div(){};
void mod(){}; 
