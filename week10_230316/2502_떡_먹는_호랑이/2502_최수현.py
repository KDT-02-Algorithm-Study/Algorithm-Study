# 메모리 31256 KB, 시간 64 ms

day, rice = map(int, input().split())

# 3 = 1 + 2
# 4 = 2 + 3(1 + 2) = 1*1 + 2*2
# 5 = 3(1 + 2) + 4(1*1 + 2*2) = 1*2 + 2*3

# 첫째날과 둘째 날의 수 tuple로 저장
#           첫째날   둘째날
rice_div = [(1, 0), (0, 1)]
for i in range(2, day):
    rice_div.append((rice_div[i-2][0]+rice_div[i-1][0], rice_div[i-2][1]+rice_div[i-1][1]))

cnt1, cnt2 = rice_div[day-1]

# 첫째날에 떡 1개부터 시작
n = 1
while 1:
    if (rice - (n * cnt1)) % cnt2 == 0:
        print(n, (rice - (n * cnt1))//cnt2, sep='\n')
        break
    else:
        n += 1