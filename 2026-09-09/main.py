class C:
    def __init__(self):
        self.a = 1
        self.__b = 2
    def get_b(self):
        return self.__b
    def set_b(self, v):
        self.__b = v
    b = property(get_b, set_b)
    
c = C()
print(c.a)
#print(c.get_b())
#c.set_b(42)
#print(c.get_b())
print(c.b)
c.b = 42
print(c.b)


def get_inc(diff):
    def f(x):
        return x + diff
    return f

def F(x, diff):
    return x + diff
inc2 = get_inc(2)
print(inc2(10))
print(F(10, 2))
