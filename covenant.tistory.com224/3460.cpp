#include <cstdio>

using namespace std;

int main(void){
  int t, n;
  scanf("%d",&t);
  while(t--){
    int cnt=0;
    scanf("%d",&n);

    while(n>0){
      if (n%2 ==1)
      printf("%d ", cnt);

      n/=2;
      cnt++;
    }
  }
}
