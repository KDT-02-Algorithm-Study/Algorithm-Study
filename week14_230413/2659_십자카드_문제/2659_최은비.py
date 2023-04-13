# 십자카드 문제 https://www.acmicpc.net/problem/2659
# 31256KB / 76ms
import sys
input = sys.stdin.readline

# 비교할 수가 시계수가 맞으면 true 반환
def clock_num(s):
    ans = int(1e9)
    for i in range(4):
        tmp = ''
        for j in range(4):
            tmp += s[(i+j)%4]
        
        ans = min(ans, int(tmp))
    
    if ans == int(s):
        return True
    else:
        return False


n = input().split()
num = int(1e9)
cnt = 1

# 주어진 숫자로 만들 수 있는 가장 작은 시계수 찾기
for i in range(4):
    tmp = ''
    for j in range(4):
        tmp += n[(i+j)%4]

    num = min(num, int(tmp))

# 1111부터 시계수가 몇개인지를 count
for i in range(1111, num+1):
    if clock_num(str(i)):
        if i < num:
            cnt += 1

print(cnt)