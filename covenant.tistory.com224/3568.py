import sys
input=sys.stdin.readline
arr=list(input().split())
common=arr[0]
answer=''
for i in range(1,len(arr)):
    temp=common
    a=''
    temp2=[]
    s=list(arr[i])
    while not(a.isalpha()):
        if s[-1].isalpha():
            break
        a=s.pop()
        if a==';' or a==',':
            continue
        temp2.append(a)

    temp2=''.join(temp2)
    temp2=temp2.replace("]","1")
    temp2 = temp2.replace("[", "]")
    temp2 = temp2.replace("1", "[")
    answer+=temp+temp2+' '+''.join(s)+';'+'\n'
print(answer)