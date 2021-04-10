import re

handle = open('mbox-short.rtf')
"""
print('Using method .find')
for line in handle:
    if line.find('From:') != -1:
        print(line.strip())

## uguale
for line in handle:
    line = line.rstrip()
    if re.search('From:', line):
        print(line.strip())


for line in handle:
    line = line.rstrip()
    if re.search('^From:', line): # equivalente di startswith
        print(line.strip())

il punto sta per qualsiasi numero o carattere,
l'asterisco sta per 'ripetuto n volte'.
quindi questa trova tutto ciò che inizia per X, poi ha un
qualunque carattere n volte e poi un due punti
"""
# vedi regex1.png
for line in handle:
    line = line.rstrip()
    if re.search('^X.*:', line):
        print(line.strip())


# vedi regex2.png il più serve per dirgli che non vuole spazi prima
# dei due punti
for line in handle:
    if re.search('^X-\S+:', line):
        print(line.strip())
