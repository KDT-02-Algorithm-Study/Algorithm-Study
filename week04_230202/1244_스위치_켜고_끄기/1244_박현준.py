N = int(input())
swt = [2] + [int(x) for x in input().split()]
std = int(input())
for _ in range(std):
    s, num = map(int, input().split())
    index = 1
    if s == 1:
        while num * index <= N:
            swt[num*index] ^= 1
            index += 1
    elif s == 2:
        swt[num] ^= 1        
        while 1 <= num-index and num+index <= N and swt[num-index] == swt[num+index]:            
            swt[num-index] ^= 1
            swt[num+index] ^= 1
            index += 1
for i in range(1, N, 20):
    print(*swt[i:i+20])