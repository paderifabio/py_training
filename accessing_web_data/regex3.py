import re

handle = open('mbox-short.rtf')

numlist = list()

for line in handle:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]*)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)

numlist.sort(reverse = True)

print(numlist[:3])
