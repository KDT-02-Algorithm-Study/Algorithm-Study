# 31256 KB / 40 ms

N, M = map(int, input().split())
lst = [0] + [int(x) for x in input().split()]

res = 0

def back(index, total, time):
    global res
    if time > M:
        return

    if time <= M:
        res = max(res, total)
    # +1칸으로 굴리니까 index 범위 맞추기 위해 N-1 까지 진행
    if index <= N-1:
        back(index+1, total+lst[index+1], time +1)
    # +2칸으로 굴리니까 index 범위 맞추기 위해 N-2 까지 진행
    if index <= N-2:
        back(index+2, total//2+lst[index+2], time +1)

back(0, 1, 0)
print(res)