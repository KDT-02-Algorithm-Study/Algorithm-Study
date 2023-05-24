# 20310 타노스
# 31256 KB / 44 ms

s = list(map(int, list(input())))
n = len(s)
c1 = sum(s) # 1의 개 수
c0 = (n-c1)//2 # 0의 개수//2
c1 //= 2 # 1의 개수 //2
r = set() # index를 저장

# 앞에서 부터 1의 index 저장
for i, v in enumerate(s):
    if c1 and s[i]:
        r.add(i)
        c1 -= 1

# 뒤에서 부터 0의 index 저장
for i, v in reversed(list(enumerate(s))):
    if c0 and not s[i]:
        r.add(i)
        c0 -= 1

# 저장된 인덱스 제외 출력
a = (s[i] for i in range(n) if i not in r)
print(''.join(map(str, a)))