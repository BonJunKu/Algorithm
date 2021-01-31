import sys
N, M, V = map(int, sys.stdin.readline().strip().split())
edge = [[] for _ in range(N+1)]

for __ in range(M):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    edge[n1].append(n2)
    edge[n2].append(n1)


for e in edge:
    e.sort(reverse=True)

print(edge)

def dfs():
    d_visit = []
    stack = [V]
    d_check = [0 for _ in range(N + 1)] #[1 0 0 0]
    while stack:
        v1=stack.pop()
        if not d_check[v1]: #d_check[v1]이 0이면
            d_check[v1]=1
            d_visit.append(v1)
            stack+=edge[v1]
        return d_visit

    '''
    stack 과 edge배열이 같이 있다.
    visit과 check가 있다.
    visit은 방문한 순서를 담기 위함.
    check는 방문했는지 여부를 표시하기 위함
    stack이 빌 때까지>스택에서 뺀 걸로 check 업데이트>정답에 업데이트>해당점의 edge를 stack에 업데이트
    reverse를 한 것은 pop 때문인데, pop(0)을 사용하는 것은 좋지 않다.    
    '''

def bfs():
    b_visit = []
    queue = [V]
    b_check = [0 for _ in range(N+1)]
    b_check[V] = 1
    while queue:
        v2 = queue.pop()
        b_visit.append(v2)
        for i in reversed(edge[v2]):
            if not b_check[i]:
                b_check[i] = 1
                queue = [i] + queue
    return b_visit