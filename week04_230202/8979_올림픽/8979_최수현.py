import sys

n, k = map(int, sys.stdin.readline().split())
record = {}
for _ in range(n):
    nation, g, s, b = map(int, sys.stdin.readline().split())
    record[nation] = (g, s, b)

medals = sorted(list(record.values()), reverse=True)
for i in range(len(medals)):
    if medals[i] == record[k]:
        print(i+1)
        break