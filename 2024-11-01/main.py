import random; random.seed()

n = 10

def empty(n):
    return [[' ' for _ in range(n)] for _ in range(n)]

def printboard(m):
    def line(n):
        return "+-" * n + "+"
    l = line(n)
    print(l)
    for row in m:
        print("|%s|" % '|'.join(row))
        print(l)
    
def rand_state(n):
    m = empty(n)
    for r in range(n):
        m[r][random.randrange(0, n)] = 'Q'
    return m

if __name__ == '__main__':
    m = rand_state(n)
    printboard(m)
