import math
import random
random.seed()

#def isprime(n):
#    for d in range(2, int(math.sqrt(n))):
#        if n % d == 0:
#            return False
#    return True
#        
#n = int(input())
#if isprime(n):
#    print("prime")
#else:
#    print("not prime")
#

xs = ['a', 1.5, True, 42]
for i in range(20):
    x = random.randrange(0, 10)
    print(x, type(x))
    y = random.choice(xs)
    print(y, type(y))
