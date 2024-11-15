from Bio import SeqIO

sequences = []
for record in SeqIO.parse("/home/elenadg04/PoC2/rosalind_lcsm.txt", "fasta"):
    sequences.append(str(record.seq))

def Common_sub(sequences):
    shortest= min(sequences, key=len)
    length = len(shortest)

    for sub_lenght in range(length, 0, -1):
       for start in range(length - sub_lenght + 1):
           sub_seq = shortest[start:start + sub_lenght]

           if all(sub_seq in seq for seq in sequences):
                return sub_seq
    return "" 
           
result = Common_sub(sequences)
print(result)           