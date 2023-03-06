# https://www.acmicpc.net/problem/8979

import sys
input = sys.stdin.readline

num, ques = map(int, input().split())
ranking = [list(map(int, input().split())) for _ in range(num)]
ranking_dict = {}
ans = 0

# 0번째 수는 국가 이름(?)이니까 빼고 정렬
ranking = sorted(ranking, key=lambda x: (x[1], x[2], x[3]), reverse=True)

# 정렬된 리스트를 순회하면서 국가 이름(0번째 요소)을 키로, 각 매달 수를 밸류로 딕셔너리에 저장
for rank in ranking:
    ranking_dict[rank[0]] = rank[1:4]

# 딕셔너리를 순회하면서 순위 매기기
for rank in ranking_dict:
    ans += 1
    if ranking_dict[rank] == ranking_dict[ques]:
        break

print(ans)