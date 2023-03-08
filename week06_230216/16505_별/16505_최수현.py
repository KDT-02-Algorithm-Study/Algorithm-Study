def star(n):
    if not n:
        return ['*']
    
    little_star = star(n-1)
    big_star = [little_star[i] + ' '*(i) + little_star[i] for i in range(2**(n-1))]
    for i in range(2**(n-1)):
        big_star.append(little_star[i])
    return big_star

n = int(input())
print(*star(n), sep='\n')