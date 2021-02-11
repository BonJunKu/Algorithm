N = int(input())
li = list(map(int,input().split()))
dp = [li[0]]

for i in range(1,N):
    if li[i] > dp[-1]:
        dp.append(li[i])
        print("li[i] 추가 i: {}, li[i] : {}, dp: {}".format(i,li[i],dp))
    else:
        j = len(dp)-1
        print("현재 j : {}".format(j))
        while j > 0:
            if dp[j-1] < li[i]:
                print("dp[j-1] : {} < li[i] : {} 이므로 break".format(dp[j-1],li[i]))
                break
            j -= 1
            print("while문 안의 j = {}".format(j))
        dp[j] = li[i]
        print("dp[j] = li[i] , {}, {}".format(dp[j],li[i]))
        print("현재 dp: ",dp)
print(dp)