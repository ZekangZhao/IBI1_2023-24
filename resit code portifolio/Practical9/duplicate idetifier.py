def identify_duplicates(gene_names):
    unique_genes = []
    duplicate_genes = []
    gene_count = {}
    
    for gene in gene_names:
        if gene in gene_count:
            gene_count[gene] += 1
        else:
            gene_count[gene] = 1
    
    for gene, count in gene_count.items():
        if count == 1:
            unique_genes.append(gene)
        else:
            duplicate_genes.append(gene)
    
    return unique_genes, duplicate_genes

# Example of how to call this function
gene_names = ['DLX5', 'DLX6', 'NBAS', 'BRCA2', 'BRCA2', 'NBAS']
unique_genes, duplicate_genes = identify_duplicates(gene_names)
print(f"Unique genes: {unique_genes}")
print(f"Duplicate genes: {duplicate_genes}")
