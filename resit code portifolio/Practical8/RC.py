seq='ATGCAATCGGTGTGTCTGTTCTGAGGGCCTAA'
dic={'A':'T','G':'C','C':'G','T':'A'}
output=''
for i in range(len(seq)):
    output+=dic[seq[i]]
print(output[::-1])