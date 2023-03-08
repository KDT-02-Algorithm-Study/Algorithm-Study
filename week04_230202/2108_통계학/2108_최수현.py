import sys

n = int(input())
nums = sorted([int(sys.stdin.readline()) for _ in range(n)])

print(round(sum(nums)/n))
print(nums[n//2])

if n == 1:
    print(nums[0])
else:
    n_cnt = {}
    for num in nums:
        if num in n_cnt:
            n_cnt[num] += 1
        else:
            n_cnt[num] = 1

    cnt_list = sorted(list(n_cnt.items()), key=lambda x: (x[1],-x[0]), reverse=True)
    if cnt_list[0][1] == cnt_list[1][1]:
        print(cnt_list[1][0])
    else:
        print(cnt_list[0][0])

print(nums[-1]-nums[0])