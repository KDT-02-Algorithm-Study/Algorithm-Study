# 14247 나무 자르기
# 41536 KB / 88 ms

n = int(input())
# 초기 높이
h = list(map(int, input().split()))
# 자라는 길이
a = list(map(int, input().split()))

# 자라는 길이 정렬
a = sorted(a)

cnt = sum(h)
for i in range(1, n):
    cnt += a[i]*i
print(cnt)

'''
 1  2  3  4  7
===============
 6  1  2  4  3      6
    3  5  8  10     3
       8  12 17     8
          16 24     16
             31     31

'''