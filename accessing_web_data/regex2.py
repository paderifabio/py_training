import re

handle = open('mbox-short.rtf')

addresses = list()
for line in handle:
    if line.startswith('From:'):
        add = re.findall('\S+@\S+', line)
        addresses.append(add)

# usando le parentesi tonde si indica cosa si vuole estrarre

x = 'From stephen.marquard@uct.ac.za'

y = re.findall('^F.* \S+@(\S+)', x)

print(y)

y = re.findall('^F.* (\S+@\S+)', x)

print(y)
# [^ ] significa tutto tranne uno spazio
y = re.findall('@([^ ]*)', x)

print(y)
