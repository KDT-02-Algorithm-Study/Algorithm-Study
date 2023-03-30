# 2343 기타 레슨
# 42340 KB / 628ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


n,m = map(int,input().split())
data = list(map(int,input().split()))

num = sum(data)

start = 0 
end = num
result = num

while start<=end:
    mid = (start+end) // 2 
    if mid < max(data):
        start = mid + 1
        continue
    cnt,tmp =1,0
    for i in range(len(data)):
        if tmp + data[i] <= mid:
            tmp += data[i]
        else:
            tmp = data[i]
            cnt += 1
    if cnt <= m:
        end = mid - 1
        result = min(result,mid)
    else:
        start = mid + 1
print(result)

'''
N,M = map(int,input().split())
blues = list(map(int,input().split()))

# N이 강의의 수, M이 블루레이 수 
# 즉 N개의 강의를 M개의 블루레이에 나눠서 담으라는 것

start = 0 # 제일 작은 블루레이 크기 
total_sum = sum(blues)
end =  total_sum
res  = total_sum

while start <= end :
    video = 0
    v = 1
    mid = int((start+end)/2)
    check = total_sum
    #print(start,end,mid)

    # 다 들어가는지? 다 안 들어가는지 확인
    for b in blues: # 123456789
        if video + b <= mid :
            video += b 
            check -= b
        else :
            #print('----')
            v += 1 
            video = 0
            video += b 
            check -= b
        #print(mid,v,video,check)
   
    # 다 못채우는 경우에는 mid를 줄여야하고..
    if v <= M :
        end = mid-1
        start = mid + 1
        res = min(res,mid)
        
    else :
        start = mid + 1 
        # if (v == M-1) and (check == 0) :
        #     print('cand',mid,v,video,check)
        #     res.append(mid)
        #     print(res)
print(res)

'''