import sys
from itertools import combinations
input = sys.stdin.readline

def convert(x): #x가 들어오면 몇번째 알파벳인지로 바꿈. a가 0.. b가 25
    return ord(x) - ord('a')

def convert_2(arr): #배열이 들어오면 해당하는 알파벳을 ON표시한 비트마스크로 바꿈.
    result = 0
    for a in arr:
        result |= (1 << a)
    return result

n, k = map(int, input().split()) #n은 총 단어 수, k는 배우는 글자 수
s = set([convert(a) for a in ['a', 'c', 'i', 'n', 't']]) #s는 5개의 기본글자를 숫자로 바꾼 배열
base = 0
for i in s:
    base |= (1 << i) #base 비트마스크에 기본 글자 하나씩 추가.
arr = [set(map(convert, input().strip())) for _ in range(n)] #arr에는 n개의 단어들이 담김.
arr_2 = [convert_2(a) for a in arr] #arr_2에는 n개의 단어들을 숫자로 바꾼 배열들이 담김.
candidates = set().union(*arr) - s #알짜 글자: candidates는 숫자 배열을 unpack하고 set화 한다음 s를 뺌 즉 ainct 빼고 나머지 글자의 숫자 집합
answer = 0
if k < 5:
    print(0) #배울 수있는 글자가 5보다 작으면 무효. 하나도 못읽음.
else:
    if len(candidates) <= (k - 5): # 배울 수 있는 기본글자 외 글자가 알짜글자를 넘으면 다 배울 수 있음. n출력
        print(n)
    else:
        for c in combinations(candidates, k - 5): #알짜 글자에서 알짜 개수만가지고 조합해서 번호를 뺌.
            temp = base
            for i in c:
                temp |= (1 << i) #temp에 베이스를 옮긴 후 추가적으로 이번 combination상에서 온 비트도 올림.

            temp ^= (1 << 26) - 1 #temp를 뒤집는다.


            answer = max(answer, sum(1 if (temp & a) == 0 else 0 for a in arr_2)) #만약 모든 단어에 대해 1이면

        print(answer)
