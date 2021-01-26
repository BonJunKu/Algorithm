import sys
x=int(sys.stdin.readline())
list=[0 for _ in range(x+1)]

for i in range(1,x+1):
    if i==1:
        list[i]=0
        continue
    list[i]=list[i-1]+1
    if i%3==0 and list[i//3]+1<list[i]:
        list[i]=list[i//3]+1
    if i%2==0 and list[i//2]+1<list[i]:
        list[i]=list[i//2]+1
print(list[x])



'''

코드 리뷰


memo = dict()   딕셔너리생성
def foo(n):     
    if n in memo:    딕셔너리 안에 있으면 밸류 리턴
        return memo[n]
    if n < 2:        1이면 0
        result = 0
    else:        없으면
        x = foo(n // 2) + n % 2 + 1
        y = foo(n // 3) + n % 3 + 1
        result = min(x, y)
        memo[5]의 값은 일단 5는 그대로는 1로갈 수 없으니
        1을 빼거나 2를 배서 3이나 4를 만들어야 한다.
        m(5)=m(2)+1+1
        m(5)=m(1)+2+1
        1,2 가 1 1 인걸 알았으니까
        2배, 3배한 24 36은 2로 결정이 된거임.
        24 36을 2 3배한 48 612
                       612 9 18은 3으로 결정
        0 1 1 2 3 
    memo[n] = result
    return result

print(foo(int(input())))



d = 0
s = {0: {int(input())}}

while 1 not in s[d]:
    d += 1
    s[d] = set()

    for n in s[d - 1]:
        s[d].add(n - 1)
        if n % 2 == 0:
            s[d].add(n // 2)
        if n % 3 == 0:
            s[d].add(n // 3)
            
    s={0:{5},1:{4},2:{3,1}...?

print(d)

'''