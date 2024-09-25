class C:
    def __init__(self, x):
        self.__x = x
    def __str__(self):
        return "%s" % self.__x
    def set_x(self, x):
        self.__x = x
    def get_x(self):
        return self.__x
    x = property(get_x, set_x)

c = C(42)
print("c:", c)
print("c.x:", c.get_x())
c.set_x(0)
print("c.x:", c.get_x())

print("c.x:", c.x)
c.x = 1
print("c.x:", c.x)

