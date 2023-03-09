# 42572 KB / 128 ms

n = int(input())
H = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

# (나무, 성장속도)를 성장속도를 오름차순으로 H_A 리스트에 담는다.
H_A = sorted([(H[i], A[i]) for i in range(n)], key=lambda x:x[1])
res = 0

# 성장속도가 가장 큰 나무를 마지막에 자르는 순으로 계산한다
for index, (tree, grow) in enumerate(H_A):
    res += tree + (grow * (index))
print(res)