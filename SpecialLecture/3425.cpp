#include <cstdio>
#define MAX 1000000000
#define ABS(a) (((a)>0) ? (a) : (-(a)))
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
//numX의 경우 값을 따로 저장해줘야하기때문에 cmd배열과 같이 가는 num배열이 필요하다. 
 


int flag;
char line[5];
int stack[1001];
int cmd[100001];
int num[100001];
int inputvalue[10001];//프로그램 수행횟수 최대 만 번  
int x;
int cmdcnt=0;
int numcnt=0;
int top=-1;

void program();
void input();

void numx(int x);
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
	//freopen("input.txt","r",stdin);
	for(;;){
	
	program();
	if (flag==-1){
		break;
	}
	
	
	input();
	
	

}
return 0;	
}
void program(){
	cmdcnt=0;
	numcnt=0;
	for(;;){

		
		scanf("%s",line);
		
		
		//num x
		if (line[0]=='N'){
		cmd[cmdcnt++]=0;
		scanf("%d",&x);
	
		num[numcnt++]=x;
		}
		//pop
		if (line[0]=='P'){
		cmd[cmdcnt++]=1;
		}
		//inv
		if (line[0]=='I'){
		cmd[cmdcnt++]=2;
		}
		//dup, div
		if (line[0]=='D'){
		if (line[1]=='U'){
		cmd[cmdcnt++]=3;
		}
		else{
		cmd[cmdcnt++]=8;
		}
		}
		//swp,sub
		if (line[0]=='S'){
		if (line[1]=='W'){
			cmd[cmdcnt++]=4;
		}
		else{
		cmd[cmdcnt++]=6;
		}
		}
		if (line[0]=='A'){
		cmd[cmdcnt++]=5;
		}
		//mul,mod
		if (line[0]=='M'){
		if (line[1]=='U'){
		cmd[cmdcnt++]=7;}
		else{
		cmd[cmdcnt++]=9;
		}
		}
		//end
		if (line[0]=='E'){
		
		return;
		}
		//quit
		if (line[0]=='Q'){
		flag=-1;

		return;
		}
	}
};

void input(){
	int N;
	scanf("%d",&N);
	for (int i=0; i<N; i++){
	scanf("%d",&inputvalue[i]);
	}
	
	for (int i=0; i<N; i++){
	top=0;
	numcnt=0;	
	stack[top]=inputvalue[i];

	
	for (int j=0; j<cmdcnt;j++){
		
		
		flag=cmd[j];
		
		
		//num x
		if (flag==0){
		
		
			numx(num[numcnt++]);
		}
		else if (top ==-1){
		flag=-2;
		break;	
		}
		else if (flag==1){
			pop();
		}
		else if (flag==2){
			inv();
		}
		else if (flag==3){
			
			dup();
		}
		else if (flag==4){
			swp();
		}
		
		else if (flag==5){
			add();
		}
		
		else if (flag==6){
			sub();
		}
		
		else if (flag==7){
			mul();
		}
		
		else if (flag==8){
			div();
		}
		else if (flag==9){
			mod();
		}
		if (flag==-2) break;

	}
	if (flag==-2||top!=0)printf("ERROR\n");
	else printf("%d\n",stack[0]);
	
	
}
	printf("\n");
}
void numx(int x){
	top++;
	if (x>MAX||top>1000){
	flag=-2;
	return;}
	stack[top]=x;

};
void pop(){
	if (top<0){
	flag=-2;
	return;
	}
	top--;
};
void inv(){
	stack[top]=-stack[top];
};
void dup(){
	top++;
	
	if (top>1000){
	flag=-2;
	return;}

	stack[top]=stack[top-1];
};
void swp(){
	int tmp= stack[top];
	stack[top]=stack[top-1];
	stack[top-1]=tmp;
};
void add(){

	long tmp = stack[top-1]+stack[top];
	if (ABS(tmp)>MAX){
		flag=-2;
		return;
	}
	stack[top-1]=(int)tmp;
	top--;
	
	};
void sub(){
	long tmp = stack[top-1]-stack[top];
	if (ABS(tmp)>MAX){
		flag=-2;
		return;
	}
	stack[top-1]=(int)tmp;
	top--;

};
void mul(){
	long tmp = (long)stack[top-1]*stack[top];
	if (ABS(tmp)>MAX){
		flag=-2;
		return;
	}
	stack[top-1]=(int)tmp;
	top--;
};
void div(){
	long tmp1, tmp2;
	int tFlag=0;
	if(stack[top]==0){
	flag=-2;
	return;
	}
	tmp1=stack[top-1];
	tmp2=stack[top];
	if (tmp1<0) tFlag++;
	if (tmp2<0) tFlag++;
	tmp1 = ABS(tmp1) / ABS(tmp2);
	if (tFlag==1) stack[top-1] = -tmp1;
	else stack[top-1]=tmp1; 
	top--;
};
void mod(){
	long tmp;
	if (stack[top]==0){
	flag=-2;
	return;
	}
	tmp=ABS(stack[top-1])%ABS(stack[top]);
	if (stack[top-1]<0) stack[top-1] = -tmp;
	else stack[top-1] = tmp;
	top--;

}; 
