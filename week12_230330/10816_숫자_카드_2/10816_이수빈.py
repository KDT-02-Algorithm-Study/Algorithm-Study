# 10816 숫자 카드 2
# 131928 KB / 3132 ms (case 1)
# 133524 KB / 3140 ms (case 2)
# 131908 KB / 3028 ms (case 3)
# 131944 KB / 3000 ms (sysline)
# 114612 KB / 3040 ms (case 4)

# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
#input = sys.stdin.readline

N = int(input().rstrip())
array = sorted(list(map(int,input().split())))
M = int(input())
M_nums = list(map(int,input().ssplit()))

def bi_sear(array,target,start,end) : 
    cnt = 0 
    while start <= end :
        mid = int((start+end)/2)
        if array[mid] == target:
            '''
            # case 1
            for i in range(mid,start-1,-1) :
                if array[i] == target:
                    cnt += 1
                else :
                    break
            for j in range(mid+1,end+1):
                if array[j] == target:
                    cnt += 1
                else :
                    break
            '''
            '''
            # case 2
            cnt = array[start:end+1].count(target)
            '''
            # case 3
            for i in range(start,end+1):
                if array[i] == target:
                    cnt += 1
            return cnt  
        
        elif array[mid] > target:
            end = mid-1
        else :
            start = mid + 1
    return cnt
d = {}
for m in M_nums:
    if m not in d:
        d[m] = bi_sear(array,m,0,N-1)
    print(str(d[m]), end = ' ')
        # print(d[m], end = ' ')
# print(' '.join(list(d.values())))

# print(' '.join(str(d[m])))# if m in d else '0' for m in M_nums))
# print(' '.join(str(d[m]) if m in d else '0' for m in M_nums))






# case 4

'''
count = {}
for card in array :
    if card in count :
        count[card] += 1
    else :
        count[card] = 1

def bi_sear(array,target,start,end) : 
    while start <= end :
        mid = int((start+end)/2)
        if array[mid] == target:
            return count.get(target)  
        
        elif array[mid] > target:
            end = mid-1
        else :
            start = mid + 1
    return 0

for m in M_nums:
    print(bi_sear(array, m, 0, N-1), end=" ")
'''