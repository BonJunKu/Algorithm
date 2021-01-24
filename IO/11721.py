import sys
a=sys.stdin.readline()
for i in range(len(a)):
    if(i%10!=9):
        print(a[i],end="")
    else:
        print(a[i])

'''
a = input()
for i in range(0,len(a),10):
    print(a[i:i+10])
'''