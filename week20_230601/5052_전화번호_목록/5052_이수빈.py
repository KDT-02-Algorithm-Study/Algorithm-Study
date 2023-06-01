# 5052 전화번호 목록
# 32276 KB / 168 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

t = int(input())
for tt in range(t):
    flag = True
    numbers = int(input())
    n_books = sorted([input().rstrip() for _ in range(numbers)])
    
    for nb in range(numbers-1):
        if n_books[nb] == n_books[nb+1][:len(n_books[nb])]:
            print('NO')
            break
    else :
        print('YES')

