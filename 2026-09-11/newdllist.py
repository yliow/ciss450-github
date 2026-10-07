def short_id(obj):
    return "...%s" % str(id(obj))[-4:]

class newdlnode:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next
    def __str__(self):
        return str(self.key)
    def __repr__(self):
        return "<newdlnode %s key:%s, prev:%s, next:%s>" % \
            (short_id(self),
             self.key,
             short_id(self.prev),
             short_id(self.next))

class DuplicateKeyError(Exception):
    pass
        
class newdllist:
    def __init__(self):
        self.head = newdlnode(None)
        self.tail = newdlnode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = {}
        self.size = 0
    def __str__(self):
        n = self.head.next
        keys = []
        while n != self.tail:
            keys.append(n.key)
            n = n.next
        return str(keys)
    def __repr__(self):
        pass
    def __len__(self):
        return self.size
    def insert_head(self, key):
        if key in self.d:
            raise DuplicateKeyError
        p = self.head
        q = newdlnode(key)
        r = self.head.next
        p.next = q; q.next = r
        r.prev = q; q.prev = p
        self.size += 1
        self.d[key] = q
    def __contains__(self, key):
        return key in self.d
    def find(self, key):
        return self.d[key]
    def update(self, key, newkey):
        n = self.find(key)
        n.key = newkey
        del self.d[key]
        self.d[newkey] = n
        
