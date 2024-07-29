import re
import blosum as bl
import os
os.chdir(r'C:\Users\Lenovo\Desktop\IBI1 notes\IBI1_2023-24\resit code portifolio\Practical13')
matrix = bl.BLOSUM(62)

with open("SOD2_human.fa", "r") as file_human:
    human = file_human.read()

with open("SOD2_mouse.fa", "r")  as file_mouse:
    mouse = file_mouse.read()

with open("RandomSeq.fa", "r") as file_random:
    random= file_random.read()

Seq1 = re.findall(r'^[^>].*', human, re.MULTILINE)
seq1 = ''.join(Seq1)

Seq2 = re.findall(r'^[^>].*', mouse, re.MULTILINE)
seq2 = ''.join(Seq2)

Seq3 = re.findall(r'^[^>].*', random, re.MULTILINE)
seq3 = ''.join(Seq3)

distance = 0

for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        distance += 1
similarity = 1 - distance / len(seq1)

score = 0
for i in range(len(seq1)):
    score += matrix[seq1[i]][seq2[i]]
print(f"Human and mouse: alignment score is {score} and identical amino acid percent is {similarity}")


distance = 0

for i in range(len(seq1)):
    if seq1[i] != seq3[i]:
        distance += 1
similarity = 1 - distance / len(seq1)

score = 0
for i in range(len(seq1)):
    score += matrix[seq1[i]][seq3[i]]
print(f"Human and random: alignment score is {score} and identical amino acid percent is {similarity}")

distance = 0

for i in range(len(seq2)):
    if seq2[i] != seq3[i]:
        distance += 1
similarity = 1 - distance / len(seq1)

score = 0
for i in range(len(seq2)):
    score += matrix[seq2[i]][seq3[i]]
print(f"random and mouse: alignment score is {score} and identical amino acid percent is {similarity}")

#human and mouse are most closely related
#human are more closely match the mouse