from Bio import SeqIO

DNA = []
for record in SeqIO.parse("/home/elenadg04/PoC2/rosalind_cons.txt", "fasta"):
    DNA.append(str(record.seq))

n = len(DNA[0])
matrix_prof =[
    [0] *n,
    [0] * n,
    [0] *n,
    [0] *n
]

for nucleotide in DNA:
    for i in range(n):
        if nucleotide[i] == 'A':
            matrix_prof [0][i] += 1
        elif nucleotide[i] == 'C':
            matrix_prof [1][i] += 1 
        elif nucleotide[i] == 'G':
            matrix_prof [2][i] += 1  
        elif nucleotide[i] == 'T':
            matrix_prof [3][i] += 1

cons = []

for i in range(n):
    counts = [matrix_prof[0][i], matrix_prof[1][i], matrix_prof[2][i], matrix_prof[3][i]]
    maximum = max(counts)   

    if counts[0] == maximum:
        cons.append('A')  
    elif counts[1] == maximum:
        cons.append('C') 
    elif counts[2] == maximum:
        cons.append('G')
    elif counts[3] == maximum:
        cons.append('T')         

print("".join(cons))

nucleotides = ['A', 'C', 'G', 'T']
for i in range(4):
    print(f"{nucleotides[i]}: {' '.join(map(str, matrix_prof[i]))}")         