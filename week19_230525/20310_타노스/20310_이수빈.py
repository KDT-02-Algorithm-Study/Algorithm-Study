# 20310 타노스
# KB / ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

num = list(input().rstrip())
num_0,num_1 = num.count('0'),num.count('1')

# 0은 뒤에서부터 빼고
for n in range(int(num_0/2)):
    idx_0 = len(num)-num[::-1].index('0')-1
    num.pop(idx_0)          

# 1은 앞에서부터 빼고
for n in range(int(num_1/2)):
    idx_1 = num.index('1')
    num.pop(idx_1)    
print(''.join(num))

