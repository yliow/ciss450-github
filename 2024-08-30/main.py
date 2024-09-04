# xs = [2, 3, 5, 7, 11, 13]
# print(xs)
# print(xs[1:5:2])

# for i in [1, 2, 3, 5, 3, 2]:
#     print(i)

# for i in [1, 2, 3, 4, 5, 6, 7, 8]:
#     print(i)
#     i -= 1

# for i in range(10):
#     print(i, end=' ')
# print()

# for i in range(2, 10):
#     print(i, end=' ')
# print()

# for i in range(2, 10, 3):
#     print(i, end=' ')
# print()

# for i in range(10, 0, -1):
#     print(i, end=' ')
# print()

# # s = float(input("gimme a float: "))
# # print(s, type(s))

# print(list(range(10)))


# names = ['john', 'tom', 'mary', 'jane', 'nobody']
# addresses = ['rogers', 'nifong', 'south', 'east'] 
# for i in range(len(names)):
#     print(i, names[i])
# for i, name in enumerate(names):
#     print(i, name)

# for i in range(len(names)):
#     print(names[i], addresses[i])

# for name, address in zip(names, addresses):
#     print(name, address)


def f(x, y):
    return x + 2 * y

print(f(y=2, x=1))

def g(a, b, *x):
    print(x, type(x))

g(1, 2, 3, 4, 5)


def h(**x):
    print(x)


xs = (1, 2, 3, 4)
print(xs)
ys = [1, 2, 3, 4]
print(ys)
ys[0] = "hello"
print(ys)
#xs[0] = "hello"

d = {}
print(d)

d['john'] = 5.14
d['tom'] = 6.24
print(d)
print(d['tom'])
for key in d:
    print(key, d[key])
for name, height in d.items():
    print(name, height)
print('tom' in d)
print('jane' in d)


