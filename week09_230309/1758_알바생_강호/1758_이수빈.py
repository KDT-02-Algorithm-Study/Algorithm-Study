# 1758 알바생 강호
# 48244 KB / 3920 ms

# 기본 코드 
import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline

# 자신이 주려고 생각했던 금액과 순서에 따라서 팁이 결정됨
# 원래 주려고 생각했던 돈 - (받은 등수 - 1) & 값이 음수가 되면 팁을 받지 못 함
# ex ) 3 - (1-1) = 3 // 3 - (2-1) = 2 // 3 - (3-1) = 1 // 3 - (4-1) = 0    => 3 + 2 + 1 + 0 = 6 원
# 이걸 잘 조합해서 제일 크게 받을 수 있도록 계산 

N = int(input())
peo = []
minus = []
for i in range(N):
    minus.append(i)
    peo.append(int(input()))
s_peo = sorted(peo)
zip_peo,zip_rs_peo = [],[]

for ai,bi in zip(s_peo,minus) :
    z = ai-bi
    if z < 0 : z = 0 
    zip_peo.append(z)
for ci,di in zip(s_peo[::-1],minus):
    z = ci-di
    if z < 0 : z = 0 
    zip_rs_peo.append(z)

print(max(sum(zip_peo),sum(zip_rs_peo)))





