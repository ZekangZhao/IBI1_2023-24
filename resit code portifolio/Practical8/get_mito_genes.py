import re
fasta_file_path = r"C:\Users\Lenovo\Desktop\IBI1 notes\IBI1_2023-24\resit code portifolio\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
genes_dict={}
fullname_dict={}
simplified_name=[]
with open(fasta_file_path, 'r',encoding='UTF-8') as fasta_file:
    for line in fasta_file:
        if line.startswith('>'):
            s=line
            fullname_dict[s]=''
            simplified_name.append(''.join(re.findall(r'gene:(.+?)\s',line)))
            genes_dict[simplified_name[-1]]=''
        else:
            genes_dict[simplified_name[-1]] += line.strip()+'\n'
            fullname_dict[s] += line.strip()+'\n'
roll=0
with open(r"C:\Users\Lenovo\Desktop\IBI1 notes\IBI1_2023-24\resit code portifolio\Practical8\mito.fa",'w',encoding='UTF-8') as f1:
        for gene_name, gene_sequence in fullname_dict.items():
            count = gene_name.count('Mito')
            if count!=0:
                f1.write('>'+simplified_name[roll]+'\n'+gene_sequence +'\n')
            roll=roll+1

