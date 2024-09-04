# main.py

# import a
# print(a)

# import sys
# sys.path.append('library')
# import b

# print(a.x)
# print(a.f(42))
# print(b.y)

# import a as A
# print(A.x)
# A.x = 42

# from a import x
# print(x)

# import a, b
# from a import x, w, f

import Rational
# from Rational import Rational

f = Rational.Rational(1, 2)
print(f)
print(repr(f))
g = Rational.Rational(2, 3)
print(f + g)

s = input("enter fraction:")
n,d = s.split('/')
#n,d = int(n),int(d)
print(n, d)
h = Rational.Rational(n, d)
print(h)
