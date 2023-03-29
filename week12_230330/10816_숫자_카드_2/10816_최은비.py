# 숫자 카드 2 https://www.acmicpc.net/problem/10816
# 118720KB / 836ms
import sys
input = sys.stdin.readline

num = int(input())
sk_cards = list(map(int, input().split()))
num2 = int(input())
cards = list(map(int, input().split()))
sk_dict = {}

for card in sk_cards:
    if card not in sk_dict:
        sk_dict[card] = 1
    else:
        sk_dict[card] += 1

for card in cards:
    print(sk_dict.get(card, 0), end=" ")


'''
이분탐색 시간초과
n = int(input())
tmp = sorted(list(map(int, input().split())))
sg = {}

for i in tmp:
    if i not in sg:
        sg[i] = 1
    else:
        sg[i] += 1

m = int(input())
target = list(map(int, input().split()))
res = []

for num in target:
    tmp = 0
    for sg_num, sg_cnt in sg.items():
        s = min(sg)
        e = max(sg)

        while s <= e:
            mid = (s + e) // 2
            if sg_num < num:
                e = mid - 1
            elif sg_num > num:
                s = mid + 1
            else:
                tmp = sg_cnt
                break      

    res.append(tmp)
    
print(*res)
'''