from Bio import SeqIO

DNA = []
for record in SeqIO.parse("/home/elenadg04/PoC2/rosalind_revp.txt", "fasta"):
    DNA = str(record.seq)


def reverse(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    return''.join(complement[base] for base in reversed(seq))

def rev_pal(DNA):
    reverse_pali = []
    n = len(DNA)

    for lenght in range(4, 13):
        for i in range(n - lenght + 1):
            sub = DNA[i:i + lenght]
            rev_sub = reverse(sub)

            if sub == rev_sub:
                reverse_pali.append((i + 1, lenght))

    return reverse_pali

result = rev_pal(DNA)

for position, length in result:
    print(position, length)           

