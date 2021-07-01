s=list(input())
stack=[]
c=0
print(stack)
for i in s:
    print('-------------')
    print(stack,i)
    if i == ')':
        t=0
        while len(stack)!=0:
            print(stack)
            top=stack.pop()
            if top=='(':
                if t==0:
                    stack.append(2)
                    print(stack)
                else:
                    stack.append(2*t)
                    print(stack)
                break
            elif top=='[':
                print(0)
                exit(0)
            else:
                print('발동')
                t=t+(top)
    elif i ==']':
        t=0
        while len(stack)!=0:
            print(stack)
            top=stack.pop()
            if top=='[':
                if t==0:
                    stack.append(3)
                    print(stack)
                else:
                    stack.append(3*t)
                    print(stack)
                break
            elif top=='(':
                print(0)
                exit(0)
            else:
                print('발동')
                t=t+(top)
    else:
        stack.append(i)
for i in stack:
    if i=='('or i=='[':
        print(0)
        exit(0)
    else:
        c+=i
print(c)


# 풀이 정리
# 1. 여는 괄호를 만나면 스택에 저장
# 2. 닫는 괄호를 만나면 짝을 만날때까지ㅏ top을 뺌.
# 3. 짝을 만나기 전 다른 괄호가 나오면 return 0
# 4. 짝을 만나기 전 숫자를 만나면 t에다가 더해서 저장
# 5. 짝을  만났을때 t가 0이면 2 또는 3 저장, t가 0이 아니면 2*t 또는 3*t 저장
# 6. 끝까지 다 돈다음에는 스택에 있는 숫자를 합침. 괄호가 남아있으면 리턴 0