# 2659 십자카드 문제
# 31256 KB / 60 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

nums = list(input().split())

def find_clock(nums):
    clocks_num = []
    for i in range(4):
        tmp = []
        for j in range(4):
            tmp.append(nums[(i+j)%4])
        clocks_num.append(int("".join(tmp)))
    min_clocks_num = min(clocks_num)

    return min_clocks_num
min_clocks_num = find_clock(nums)

cnt = 0
for i in range(1111,min_clocks_num+1):
    if '0' not in str(i):
        # 어떤 조합으로 시계수를 만들 때, 입력 값이 최소값일 때만 시계수 조건 성립
        if i == find_clock(list(str(i))):
            cnt += 1
print(cnt)
