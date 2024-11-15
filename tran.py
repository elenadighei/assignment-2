from Bio import SeqIO

DNA = []
for record in SeqIO.parse("/home/elenadg04/PoC2/rosalind_tran.txt", "fasta"):
    DNA.append(str(record.seq))

s1 = DNA[0]
s2 = DNA[1]


def tt_ratio(s1,s2):
    transitions = 0
    transversions = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if (s1[i] == 'A' and s2[i] == 'G') or (s1[i] == 'G' and s2[i] == 'A') or (s1[i] == 'C' and s2[i] == 'T') or (s1[i] == 'T' and s2[i] == 'C'):
                transitions += 1
            if (s1[i] == 'A' and s2[i] == 'C') or (s1[i] == 'A' and s2[i] == 'T')  or (s1[i] == 'G' and s2[i] == 'C') or (s1[i] == 'G' and s2[i] == 'T') or (s1[i] == 'C' and s2[i] == 'A') or (s1[i] == 'C' and s2[i] == 'G') or (s1[i] == 'T' and s2[i] == 'A') or (s1[i] == 'T' and s2[i] == 'G'):
                transversions += 1

    return transitions / transversions


result = tt_ratio(s1, s2)

print(result)                       