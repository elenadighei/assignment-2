codon_dict= {
    'A': 4,  
    'C': 2,
    'D' : 2,
    'E' : 2,
    'F' : 2,
    'H' : 2,
    'G' : 4,
    'I' : 3,
    'K' : 2,
    'L' : 6,
    'M' : 1,
    'N' : 2,
    'P': 4,
    'Q' : 2,
    'R' : 6,
    'S': 6,
    'T' : 4,
    'V': 4,
    'W' : 1,
    'Y' : 2.
}

n = 1
prot = input()

for amino in prot:
       n *= codon_dict[amino]
       n %= 1000000


result = (n * 3)  % 1000000

print(result)    