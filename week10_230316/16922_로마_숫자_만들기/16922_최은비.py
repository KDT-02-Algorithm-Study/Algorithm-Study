# 16922 로마 숫자 만들기 https://www.acmicpc.net/problem/16922
# 31256KB / 44ms
import sys
input = sys.stdin.readline

def roma_num(cnt, start):
    global tmp 

    if cnt == n:
        check[tmp] = 1
        return

    # 이전에 조합했던 수는 다시 조합하지 않기 위한 출발점 조정
    for i in range(start, 4):
        tmp += num[i]
        roma_num(cnt+1, i)
        tmp -= num[i]


n = int(input())
num = [1, 5, 10, 50]
# 중복되는 수 무시하기 위한 리스트
# (1, 5) (5, 1)은 둘 다 6인데 한 번만 카운트 해야 함
check = [0] * 1001
tmp = 0

roma_num(0, 0)
print(sum(check))