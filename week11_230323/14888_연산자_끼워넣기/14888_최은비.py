# 연산자 끼워넣기 https://www.acmicpc.net/problem/14888
# 31256KB / 96ms
import sys
input = sys.stdin.readline

def exp(cnt):
    if cnt == n-1:
        tmp = number[0]
        for i in range(n-1):
            if order[i] == 0:
                tmp += number[i+1]
            elif order[i] == 1:
                tmp -= number[i+1]
            elif order[i] == 2:
                tmp *= number[i+1]
            else:
                if tmp < 0:
                    tmp = (tmp * (-1) // number[i+1]) * (-1)
                else:
                    tmp //= number[i+1]

        # 만들 수 있는 모든 연산 결과를 append
        res.append(tmp)
        return

    for i in range(4):
        # 주어진 연산자들을 다 사용할 때까지 반복
        # 인덱스를 연산자로 생각하고 리스트에 append
        if oper[i]:
            order.append(i)
            oper[i] -= 1
            exp(cnt+1)
            oper[i] += 1
            order.pop()
            

n = int(input())
number = list(map(int, input().split()))
oper = list(map(int, input().split()))
order = []
res = []

exp(0)

# 최소값과 최대값이 같으면 하나만 출력
if len(res) == 1:
    print(*res, *res, sep="\n")
else:
    print(max(res))
    print(min(res))