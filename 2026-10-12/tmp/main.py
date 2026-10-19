print(eval("1 + 2"))
x = 1
y = 2
print(eval("x + y"))
z = eval("x + y")
print(z, type(z))
a = 3
b = 2
exec("z = a + b")
print(z, type(z))

C = "X0 != X1"
print(C, type(C))
C1 = C.replace("X0", "0").replace("X1", "2")
