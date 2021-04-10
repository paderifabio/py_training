## training on for loops

import random

start = 0
for i in [1,50,45,4,10]:
    if i > start:
        start = i
    print(start, i)
print('largest is:',start)


# conteggio degli elementi
start = 0
for i in [1,2,3,5,2,3,6,2,4,6,2,5,2]:
    start = start + 1
print(start)

# finding the smallest value
smallest = None
for i in [3,4,10,49,100,43,123,31,543]:
    if smallest is None :
        smallest = i
    elif i < smallest:
        smallest = i
print(smallest)




