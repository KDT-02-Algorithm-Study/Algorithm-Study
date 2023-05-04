# 추월 https://www.acmicpc.net/problem/2002
# 31256KB / 120ms
import sys
input = sys.stdin.readline

n = int(input())
start = [input().strip() for _ in range(n)]
end = [input().strip() for _ in range(n)]
cnt = 0
check = [False] * n

# 같은 차량이 나오기 전에 다른 차가 먼저 나오면 추월 당한 것 > cnt 증가
# 중복 방지를 위한 리스트 check

for i in range(n):
    for j in range(n):
        if start[i] == end[j]:
            check[j] = True
            break
        else:
            if not check[j]:
                cnt += 1
                check[j] = True

print(cnt)

'''
start
ZG508OK
PU305A
RI604B
ZG206A
ZG232ZF

end
PU305A
ZG232ZF
ZG206A
ZG508OK
RI604B

i:    ZG508OK  PU305A  RI604B  ...
j:    PU305A   PU305A  PU305A
      ZG232ZF          ZG232ZF
      ZG206A           ZG206A
                       ZG508OK
cnt:  3        3       3        ...
'''