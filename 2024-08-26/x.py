def f(x):
    assert x == 0, "bad %s" % x
    return 42


f(0)
f(1)

print("hello world")
print('h')
x = "hello world"
print(x, type(x), id(x))
x = 1
print(x, type(x), id(x))

i = int(input("gimme i: "))
print(i, type(i))
j = int(input("gimme j: "))
print(j, type(j))
print(i, "+", j, "=", i + j)
print(i, "-", j, "=", i - j)
print(i, "*", j, "=", i * j)
print(i, "/", j, "=", i / j)
print(i, "//", j, "=", i // j)
print(i, "%", j, "=", i % j)
x = True
y = True
x = (i == j)
