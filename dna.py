# 
# Jordan Campbell
# 19 February 2020
# Count the number of occurances of the characters 'A', 'C', 'G', 'T' in a string.

with open("dna.txt", 'r') as fh:
    data = fh.read()

A = 0
C = 0
G = 0
T = 0
for c in data:
    if c == 'A': 
        A += 1
    if c == 'G':
        G += 1
    if c == 'C':
        C += 1
    if c == 'T':
        T += 1

print(A, C, G, T)