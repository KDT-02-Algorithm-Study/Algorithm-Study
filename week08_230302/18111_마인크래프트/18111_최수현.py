# 메모리 31256 KB, 시간 148 ms
import sys
intput = sys.stdin.readline

n, m, b = map(int, input().split())

# 그라운드 딕셔너리에 땅의 높이 별 개수 저장
ground = {}
for _ in range(n):
    for num in list(map(int, input().split())):
        if num in ground:
            ground[num] += 1
        else:
            ground[num] = 1
time = 0
# 가장 높은 땅, 가장 낮은 땅의 높이와 각각의 개수
max_n = max(ground.keys())
max_cnt = ground[max_n]
min_n = min(ground.keys())
min_cnt = ground[min_n]

while 1:
    # 땅높이 같으면 반복문 종료
    if min_n == max_n:
        break
    
    # 높은 땅을 깎는 시간과 낮은 땅을 채우는 시간 비교
    # 같은 경우는 땅을 더 높여야하므로 첫 if문에 해당되도록함
    # 낮은 땅을 채우는 시간이 더 적더라도 인벤토리의 수를 봐야 함
    if max_cnt*2 >= min_cnt and b >= min_cnt:
        b -= min_cnt
        time += min_cnt
        min_n += 1
        # ground에 +1 한 만큼의 땅높이가 있다면 min_cnt에 추가
        if min_n in ground:
            min_cnt += ground[min_n]
    else:
        b += max_cnt
        time += max_cnt * 2
        max_n -= 1
        # ground에 -1 한 만큼의 땅높이가 있다면 min_cnt에 추가
        if max_n in ground:
            max_cnt += ground[max_n]

print(time, min_n)