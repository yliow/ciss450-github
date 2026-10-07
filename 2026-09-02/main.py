def bubblesort(xs):
    pass

def mergesort(xs):
    pass

if __name__ == '__main__':
    print("__name__ ...")
    xs = [5, 3, 1, 2, 4, 9, 8, 5, 7]
    n = len(xs)
    
class X:
    def __init__(self, a, b, c):
        self._a = a
        self._b = c
        self._c = c
    def __str__(self):
        return "<X a=%s, b=%s, c=%s>" % (self._a, self._b, self._c)

class Y(X):
    def __init__(self):
        pass
    
obj = X(3, 2.14, "cat")
print(obj)
print(obj.d)
