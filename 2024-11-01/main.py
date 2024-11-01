import random; random.seed()

n = 5

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

def isdiag(p0, p1):
    r0,c0 = p0
    r1,c1 = p1
    dr = r0 - r1
    dc = c0 - c1
    return dr == dc or dr == -dc

def isattacking(p0, p1):
    return isdiag(p0, p1) or p0[1] == p1[1]

def h(m):
    n = len(m)
    points = []
    for r,row in enumerate(m):
        for c, v in enumerate(row):
            if m[r][c] == 'Q':
                points.append((r, c))
    print(points)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            p0 = points[i]
            p1 = points[j]
            print((i, j), p0, p1, isattacking(p0, p1))

if __name__ == '__main__':
    m = rand_state(n)
    printboard(m)
    h(m)
