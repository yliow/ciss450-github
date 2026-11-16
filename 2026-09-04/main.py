from sllist import sllist

xs = sllist()
print(xs)

print("None is at", id(None))
xs.insert_head(3)
print(xs)

xs.insert_head(0)
print(xs)
