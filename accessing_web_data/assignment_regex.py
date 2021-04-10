
import re

handle = open('regex_sum_508654.txt')

numlist = list()
for line in handle:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    if len(num) < 1 : continue
    for i in num:
        flnum = float(i)
        numlist.append(flnum)

print(sum(numlist))
