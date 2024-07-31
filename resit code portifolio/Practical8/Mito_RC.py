filename=input('filename:')
filename=filename+str('.fa')
import re
import os
os.chdir(r'C:\Users\Lenovo\Desktop\IBI1 notes\IBI1_2023-24\resit code portifolio\Practical8')
def reverse(seq): 
    x=''
    seq=seq[::-1]
    for i in range(len(seq)):
        if seq[i]=='A':
            x+='T'
        if seq[i]=='C':
            x+='G'
        if seq[i]=='T':
            x+='A'
        if seq[i]=='G':
            x+='C'
    return(x)

name=[]
sequence={}
length={}
with open('mito.fa','r',encoding='UTF-8') as fasta_file:
    for line in fasta_file:
        if line.startswith('>'):     #record the gene name
            gene_name=line.strip()
            name.append(gene_name)
            sequence[gene_name]=''
        else:
            sequence[gene_name]+=line.strip()
roll=0
with open(filename,'w',encoding='UTF-8') as output_file:
    for gene,sequence in sequence.items():
        output_file.write(gene+'  length:'+str(len(sequence))+'\n'+reverse(sequence)+'\n')
        roll+=1
with open(filename,'r',encoding='UTF-8') as f1:
       print(f1.read())
