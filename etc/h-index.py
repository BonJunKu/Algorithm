https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    h=[]
    answer = 0
    for i in range(0,max(citations)+1):
        cnt=0
        for j in citations:
            if j>=i:
                cnt+=1
        if cnt>=i:
            h.append(i)
        if not h:
            return 0
    return max(h)