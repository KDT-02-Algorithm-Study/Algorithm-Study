# 16922 로마 숫자 만들기
# 31256 KB / 64 ms

n = int(input())

r = set()
for i in range(n+1): # I
    for j in range(n+1): # V
        for k in range(n+1): # X
            for l in range(n+1): # L
                if i + j + k + l == n: # 개 수의 합이 n일 때만
                    r.add(i+j*5+k*10+l*50)

print(len(r))
