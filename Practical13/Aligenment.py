import blosum as bl

def read_fasta_file(fasta_file_path):
    with open(fasta_file_path, 'r') as file:
        sequence_data = []
        sequence_description = None
        sequence_lines = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence_description is not None:
                    sequence_data.append((sequence_description, ''.join(sequence_lines)))
                sequence_description = line[1:]  # Remove the '>'
                sequence_lines = []
            else:
                sequence_lines.append(line)
        # Add the last sequence
        sequence_data.append((sequence_description, ''.join(sequence_lines)))
    return sequence_data

# Read the sequences from the FASTA files
file_human = read_fasta_file(r"C:\Users\Lenovo\Downloads\human_sequence.fasta")
file_mouse = read_fasta_file(r"C:\Users\Lenovo\Downloads\mouse_sequence.fasta")
file_rat = read_fasta_file(r"C:\Users\Lenovo\Downloads\rat_sequence.fasta")

# Extract the sequences
human_seq, mouse_seq, rat_seq = file_human[0][1], file_mouse[0][1], file_rat[0][1]

# Calculate edit distances
edit_distance_mouse_rat = sum(1 for a, b in zip(mouse_seq, rat_seq) if a != b)
edit_distance_human_rat = sum(1 for a, b in zip(human_seq, rat_seq) if a != b)
edit_distance_human_mouse = sum(1 for a, b in zip(human_seq, mouse_seq) if a != b)

# Calculate percentage identities
min_length = min(len(human_seq), len(mouse_seq), len(rat_seq))
percentage_identity_mouse_rat = 100 - (edit_distance_mouse_rat / min_length) * 100
percentage_identity_human_rat = 100 - (edit_distance_human_rat / min_length) * 100
percentage_identity_human_mouse = 100 - (edit_distance_human_mouse / min_length) * 100

# Print edit distances and percentages
print(f"Edit distance between mouse and rat: {edit_distance_mouse_rat}")
print(f"Percentage identity between mouse and rat: {percentage_identity_mouse_rat}")

print(f"Edit distance between human and rat: {edit_distance_human_rat}")
print(f"Percentage identity between human and rat: {percentage_identity_human_rat}")

print(f"Edit distance between human and mouse: {edit_distance_human_mouse}")
print(f"Percentage identity between human and mouse: {percentage_identity_human_mouse}")

# BLOSUM62 score calculations
matrix = bl.BLOSUM(62)
human_mouse_score = calculate_blosum_score(human_seq, mouse_seq, matrix)
human_rat_score = calculate_blosum_score(human_seq, rat_seq, matrix)
mouse_rat_score = calculate_blosum_score(mouse_seq, rat_seq, matrix)

print(f"BLOSUM62 score between human and mouse: {human_mouse_score}")
print(f"BLOSUM62 score between human and rat: {human_rat_score}")
print(f"BLOSUM62 score between mouse and rat: {mouse_rat_score}")