#include <cstdio>
#include <algorithm>
using namespace std;

char inp[32]; //input
int lev; //level
int cost[32]; 
char st[32];
int top;

int main() {
	scanf("%s", inp + 1); //
	for (int i = 1; inp[i]; i++) {
		if (inp[i] == '(' || inp[i] == '[') {
			st[++top] = inp[i];
			lev++;
		}
		else {
			if ((st[top] == '(' && inp[i] == ')') ||
				(st[top] == '[' && inp[i] == ']')) {
				cost[lev - 1] += (cost[lev] ? cost[lev] : 1) * (st[top--] == '(' ? 2 : 3);
				cost[lev--] = 0;
			}
			else return !printf("0");
		}
	}
	printf("%d", cost[0]);
}
