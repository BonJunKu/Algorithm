# https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import defaultdict
def solution(clothes):
    answer = 0
    int_dict=defaultdict(int)
    for i in clothes:
        int_dict[i[1]]+=1
    multiple=1
    for k in int_dict.values():
        multiple*=(k+1)
    return multiple-1