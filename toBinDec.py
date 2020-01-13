from array import *

def toBin(n):

    if n / 2 > 0:

       toBin(n / 2)

    print n % 2

def _toBin(n):

    arr = []

    for i in range(15, -1,-1):

        arr.append(((n >> i)&1))

    print ''.join([str(x) for x in arr])

def toDec(n):
 
    base, dec = 0, 0

    while n > 0:
    	
       dec = dec + n % 2 * pow(2, base)
       base = base + 1
       n = n / 10
 
    print dec

toDec(11111)    
toDec(10000)    

