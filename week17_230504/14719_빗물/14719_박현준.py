# 31256 KB / 44 ms

H, W = map(int, input().split())
lst = [int(x) for x in input().split()]

res = 0

# 양 끝은 제외
for i in range(1, W-1):
    
    # 현재 위치 기준으로 왼쪽과 오른쪽의 최대 값을 구함
    left = max(lst[:i])
    right = max(lst[i+1:])
    
    # 두개의 값 중에서 작은 값을 구함 (그 높이만큼 물이 찰 가능성)
    water_height = min(left, right)
    
    # 현재 위치의 높이가 물의 높이보다 낮으면 물이 고임
    if lst[i] < water_height:
        
        # 차이만큼 res에 저장
        res += water_height - lst[i]
print(res)