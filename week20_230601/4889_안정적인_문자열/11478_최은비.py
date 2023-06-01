# 서로 다른 부분 문자열의 개수 https://www.acmicpc.net/problem/11478
# 239368KB / 884ms

import sys
input = sys.stdin.readline

s = input().strip()
word = {}

for i in range(len(s)):
    for j in range(len(s)):
        if i+j < len(s) and s[i:i+j+1] not in word:
            word[s[i:i+j+1]] = 1

print(len(word))