from Bio import SeqIO

DNA = []
for record in SeqIO.parse("/home/elenadg04/PoC2/rosalind_splc.txt", "fasta"):
    DNA.append(str(record.seq))


DNA_string = DNA[0]
introns = DNA[1:]

for intron in introns:
    DNA_string = DNA_string.replace(intron, "")

RNA_string =[]

for nucleotide in DNA_string:
    if nucleotide == 'A':
        RNA_string.append('A')
    elif nucleotide == 'C':
        RNA_string.append('C')
    elif nucleotide == 'G':
        RNA_string.append('G')
    elif nucleotide == 'T':
        RNA_string.append('U')

RNA_string = ''.join(RNA_string)


def Prot(RNA_string):

    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C',  'UGA' : 'Stop',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
        'UGG': 'W'
    }


    protein =  []
    
    for i in range(0, len(RNA_string), 3):
        codon = RNA_string[i:i+3]

        if codon in codon_table:
            amino = codon_table[codon]
        
        if amino == 'Stop':
            break
    
        protein.append(amino)
    return ''.join(protein)


result = Prot(RNA_string)
print(result)