__author__ = 'bijan'
import math

s = raw_input().strip()
l = len(s)

sroot = math.sqrt(l)
row = int(math.floor(sroot))
col = int(math.ceil(sroot))

if row * col < l:
    row +=1

text = ''
for c in range(col):
    if text != '':
        text  = text + " "
    for r in range(row):
        index = c + r * col
        if index < l:
            text = text + s[index]

print text