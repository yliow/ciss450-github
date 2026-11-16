from newdllist import *
node = newdlnode
dllist = newdllist

"""
n = node(4)
print(n)
print(repr(n))
"""

xs = dllist()
print(xs, len(xs))

xs.insert_head(42)
print(xs, len(xs))

xs.insert_head(-1)
print(xs, len(xs))

xs.insert_head(5)
print(xs, len(xs))

for x in [42, -1, 5, 10000]:
    print(x in xs)

n = xs.find(42)
print(n, type(n))

#n = xs.find(10000)
#print(n, type(n))

xs.update(5, 55)
print(xs)
