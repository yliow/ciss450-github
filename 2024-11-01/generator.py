def get_next():
    for i in range(10):
        yield i

print("test 1")
for i in get_next():
    print(i)
    
print("test 2")  
for i in get_next():
    print(i)
    if i == 5: break
    

class Range10:
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i < 10:
            ret = self.i
            self.i += 1
            return ret
        else:
            raise StopIteration

print("test 3")
for i in Range10():
    print(i)
print("test 4")
for i in Range10():
    print(i)
    if i == 5: break
        
