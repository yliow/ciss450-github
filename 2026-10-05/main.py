"""
nqueens problem using local search
"""
import random
seed = int(input("seed: "))
random.seed(seed)
n = int(input("n: "))

def tostring(s):
    n = len(s)
    ret = []
    def f(_):
        if _ == '': return '.'
        else: return _
    for r in s:
        r = [f(_) for _ in r]
        ret.append(''.join(r))
    return '\n'.join(ret) 

def random_state(n):
    s = [['' for _ in range(n)] for _ in range(n)]
    for c in range(n):
        r = random.randrange(n)
        s[r][c] = 'Q'
    return s

def h(s):
    n = len(s)
    r = [0 for _ in range(n)] # r[0] is the row of Q at column 0
    for c in range(n):
        for i in range(n):
            if s[i][c] == 'Q':
                r[c] = i
                break
    #for i,c in enumerate(r):
    #    print(i, c)

    s = 0
    for c0 in range(n):
        for c1 in range(c0 + 1, n):
            dc = c1 - c0
            dr = r[c1] - r[c0]
            if dr == 0 or \
               dc == dr or \
               dc == -dr:
                s += 1
                #print(c0, c1, r[c0], r[c1], s)
    return s
    '''
    increment h by 1 if
    r[c0] == r[c1] or
    c1 - c0 == r[c1] - r[c0]
    c1 - c0 == -(r[c1] - r[c0])
    '''

def actions(s):
    ''' all actions '''
    ret = []
    for c in range(n):
        for r in range(n):
            if s[r][c] != 'Q':
                ret.append((r,c))
    return ret

def rand_action(s):
    while 1:
        r = random.randrange(n)
        c = random.randrange(n)
        if s[r][c] != 'Q':
            return [r,c]

def result(s, a):
    n = len(s)
    ret = [r[:] for r in s]
    r, c = a
    for _ in range(n):
        ret[_][c] = ''
    ret[r][c] = 'Q'
    return ret

def hc(n):
    s0 = random_state(n)
    h0 = h(s0)
    print(tostring(s0), "h0:", h0, '\n')
    while 1:
        found = False
        for a in actions(s0):
            s1 = result(s0, a)
            h1 = h(s1)
            print(tostring(s1), "h1:", h1, '\n')
            if h1 < h0:
                s0 = s1
                h0 = h1
                print("FOUND\n", end='')
                print(tostring(s0), "h0:", h0, '\n')
                found = True
                break
        if not found:
            break
    print("FINAL\n", end='')
    print(tostring(s0), "h0:", h0, '\n')
            
if __name__ == '__main__':
    #s = random_state(n)
    #print(tostring(s))
    #h(s)
    hc(n)
