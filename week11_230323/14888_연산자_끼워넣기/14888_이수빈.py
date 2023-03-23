# 14888 연산자 끼워넣기
# 31256 KB / 56 ms 

# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N = int(input())
nums = list(map(int,input().split()))
plus,minus,mul,div = map(int,input().split())

res_max = -1e9
res_min = 1e9

def dfs(depth,number,pl,mi,mu,di):
    global res_min, res_max

    # 숫자를 다 사용했으면 
    if depth == N :
        if number > res_max :
         res_max = number
        if number < res_min : 
         res_min = number
         return

    if pl >= 1 :
        dfs(depth+1,number+nums[depth],pl-1,mi,mu,di)
    if mi >= 1 :
        dfs(depth+1,number-nums[depth],pl,mi-1,mu,di)
    if mu >= 1 :
        dfs(depth+1,number*nums[depth],pl,mi,mu-1,di)
    if di >= 1 :
        dfs(depth+1,int(number/nums[depth]),pl,mi,mu,di-1)
    
dfs(1,nums[0],plus,minus,mul,div)

print(res_max)
print(res_min)


'''
#res_max = []#-1e9
#res_min = []#1e9
res = [] 

def dfs(number,pl,mi,mu,di):
    global res # res_min, res_max

    # 숫자를 다 사용했으면 
    if pl + mi + mu + di < 0  :
        return
    
    res.append(number) #= max(res_max,number)
    #res_min = min(res_min,number)
    #print('res',res)

    for i in range(N-1):
        #print(i)
        #print(number)
        if pl >= 1 :
            number += nums[i+1]
            dfs(number,pl-1,mi,mu,di)
            #print('pl',number)
        if mi >= 1 :
            number -= nums[i+1]
            dfs(number,pl,mi-1,mu,di)
            #print('mi',number)
        if mu >= 1 :
            number *= nums[i+1] 
            dfs(number,pl,mi,mu-1,di)
            #print('mu',number,nums[i+1])
        if di >= 1 :
            number = number//nums[i+1] 
            dfs(number,pl,mi,mu,di-1)
            #print('di',number)
    
dfs(nums[0],plus,minus,mul,div)
print(max(res[1:]))
print(min(res[1:]))

# print(res_max,res_min)
'''