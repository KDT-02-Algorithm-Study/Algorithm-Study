# 32276 KB / 188 ms
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    num = [input().rstrip() for _ in range(n)]
    num.sort() # 문자열 정렬

    # 바로 앞뒤의 문자열만 비교하면 됨
    for j in range(n-1):
        # 길이를 먼저 확인해서 다음 문자열의 길이가 긴 경우에만 포함관계 확인
        if len(num[j]) <= len(num[j+1]) and num[j] == num[j+1][:len(num[j])]:
            print('NO')
            break
    else:
        print('YES')


"""
911             911
976259     =>   91125426
91125426        976259

문자열 sort 시 문자열의 길이와 상관 없이
index 0부터 시작해서 작은 순서로 정렬됨
"""