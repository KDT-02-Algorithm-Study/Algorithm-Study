# 31256 KB / 68 ms

def find(lst):
    # 네 방향의 수를 넣을 tmp 변수 
    tmp = ''
    # 네 방향의 수들 중 최소값을 찾아야 하기에 첫 번째 수를 기준으로 비교
    min_num = int(''.join(map(str, lst)))
    # 네 방향으로 탐색하여 가능한 시계수들을 탐색
    for i in range(4):
        for j in range(i, (i+4)):
            # 인덱스가 넘어가지 않도록 modular 연산을 통해 tmp에 저장
            tmp += str(lst[j%4])
        # 그 중 최솟값을 저장
        if min_num > int(tmp):
            min_num = int(tmp)
        # tmp 초기화
        tmp = ''
    # 시계수 반환
    return min_num


lst = [int(x) for x in input().split()]
cnt = 1

# 1111부터 찾을 시계수 까지
for i in range(1111, find(lst)):
    # 0이 있거나 시계수에 중복이면 continue
    if '0' in str(i) or i != find(list(str(i))):
        continue
    cnt += 1

print(cnt)