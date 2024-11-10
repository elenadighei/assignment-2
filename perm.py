

def Perm(numbers):
    if len(numbers) == 1:
        return [numbers]
    
    perms = []
    for i in range(len(numbers)):
        current = numbers[i]
        rest = numbers[:i] + numbers[i+1:]
        
        for p in Perm(rest):
            perms.append([current] + p)
    
    return perms

def print_perm(n):
    n = int(n)
    numbers = list(range(1, n + 1))
    
    perms = Perm(numbers)
    
    print(len(perms))
    
    for perm in perms:
        print(" ".join(map(str, perm)))

n = input()
print_perm(n)
    