def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result 

def binom(n, k):
    return fact(n) // (fact(k) * fact(n -k))

def binom_prob(k, m):
    n = 2 ** k
    prob = binom(n, m) * (1 / 4) ** m * (3 / 4) ** (n - m)
    return prob

def prob_N(k, N):
    total_prob = 0
    for m in range(N, 2 ** k + 1):
        total_prob += binom_prob(k, m)

    return total_prob

k, N = map(int, input().split())
res = prob_N(k, N)
print(res)    
