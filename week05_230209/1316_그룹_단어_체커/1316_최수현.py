import sys

n = int(input())
cnt = 0
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                break
    else:
        cnt += 1
print(cnt)