class slnode:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next
    def __str__(self):
        return "<slnode %s key=%s next=%s>" % (id(self),
                                               self.key,
                                               id(self.next))
class sllist:
    def __init__(self):
        self.head = None
    def __str__(self):
        s = ''
        #xs = []
        n = self.head
        while n != None:
            s += str(n) + '\n'
            xs.append(n)
            n = n.next
        s = '\n'.join([str(x) for x in xs])
        return "<sllist %s %s>" % (id(self), s) 
    def insert_head(self, key):
        self.head = slnode(key, self.head)
        
if __name__ == "__main__":
    n = slnode(42)
    print(n)
    print("None addr:", id(None))
