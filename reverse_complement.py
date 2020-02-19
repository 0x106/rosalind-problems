# 
# Jordan Campbell
# 19 February 2020
# Reverse a string then take the complement values ('A' - 'T', 'C' - 'G')

with open("reverse_complement.txt", 'r') as fh:
    src = fh.read()

print(src)
print("---------")

reverse = src[::-1]

dst = ""
for c in reverse:
    if c == 'A': 
        dst += 'T'
    if c == 'G':
        dst += 'C'
    if c == 'C':
        dst += 'G'
    if c == 'T':
        dst += 'A'

print(reverse)
print("---------")
print(dst)
