#include <cstdio>
//��� ��ȣ 
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

//������ ũ�� : 1000�� �̻��� �Ѿ�� ��� �����Ƿ� 0~1000
//������ ����:  10���� �ѱ�� �����̹Ƿ� int�� Ŀ�� ����
//����� ���� = �ִ� 100000��
//���α׷� ����Ƚ��: �ִ� 10000��

//�Է� ������ Ŀ�ǵ尡 �� ������ ���� �־����� �����̱� ������, 
//��� ��ü�� �迭�� ��Ƽ� �����ؾ� ��. ����� �ִ� ���� = 10^5 
 


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
