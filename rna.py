# 
# Jordan Campbell
# 19 February 2020
# Switch all 'T' values to be 'U'.

with open("rna.txt", 'r') as fh:
    src = fh.read()

dst = ""
for c in src:
    if c != 'T':
        dst += c
    else:
        dst += 'U'

print(src)
print(dst)
