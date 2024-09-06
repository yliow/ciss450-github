# x = set()
# print(x, type(x))
# x.add(1)
# print(x)
# x.add(2)
# print(x)
# x.add(1)
# print(x)
# x.add(1)
# print(x)
# print(dir(x))
# print(x.issubset.__doc__)

class P:
    def __init__(self, y):
        self.y = y

    def m(self):
        raise NotImplementedError("P.m child %s has problems ...." % self)
        
class C(P):
    def __init__(self, x, y):
        P.__init__(self, y)
        self.x = x

    def m(self):
        print("C.m")

class C1(P):
    def __init__(self, x, y):
        P.__init__(self, y)
        self.x = x

c = C(1, 2)
print(c.x)
print(c.y)
c1 = C1(1, 2)
c1.m()
