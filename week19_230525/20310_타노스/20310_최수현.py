# 31256 KB / 44 ms

S = list(input())
zero = S.count('0')//2  # 절반 개수
one = S.count('1')//2
z_cnt = o_cnt = 0
ans = ''

for s in S:
    # 0은 zero 개수까지만 ans 더하기
    if s == '0':
        if z_cnt < zero:
            ans += s
            z_cnt += 1
        else:
            continue
    # 1은 one 개수가 지나면 그때 부터 ans에 더하기
    else:
        if o_cnt >= one:
            ans += s
        else:
            o_cnt += 1
print(ans)