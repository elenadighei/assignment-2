def fib_rabbits_death(n, m):
    
    F = [0]*m
    F[0] = 1
    
    for month in range(1, n):

        babies = sum(F[1:])
    
        for i in range(m - 1, 0, -1):
            F[i] = F[i - 1]

        F[0] = babies
    
    return sum(F)

n, m = map(int, input().split())
result = fib_rabbits_death(n, m)
print(result)
    