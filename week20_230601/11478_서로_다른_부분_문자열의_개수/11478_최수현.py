# 240848 KB / 500 ms
import sys
input = sys.stdin.readline

s = input().rstrip()
# 전체 문자열 넣고 시작
parts = {s}
for l in range(1, len(s)): # 자릿수
    for i in range(len(s)-l+1): # 인덱스
        parts.add(s[i:i+l])

print(len(parts))