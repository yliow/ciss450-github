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
    line = '+' + (n * '-+')
    def f(_):
        if _ == '': return '.'
        else: return _
    ret.append(line)
    for r in s:
        r = [f(_) for _ in r]
        ret.append('|' + '|'.join(r) + '|' + '\n' + line)
    return '\n'.join(ret) 

def rand_state(n):
    ret = [['' for c in range(n)] for r in range(n)]
    #print(tostring(ret))
    for c in range(n):
        r = random.randrange(0, n)
        ret[r][c] = 'Q'
    #print()
    #print(tostring(ret))
    return ret


def h(s):
    n = len(s)
    r = [0 for _ in range(n)] # r[0] is the row of Q at column 0
    # r gives the row for a column c where there's a queen
    # r[2]
    for c in range(n):
        for i in range(n):
            if s[i][c] == 'Q':
                r[c] = i
                break
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
    """
    An action is (r,c) to place a queen.
    """
    n = len(s)
    ret = []
    for c in range(n):
        for r in range(n):
            if s[r][c] = '':
                ret.append((r,c))
    return ret

def result(s, a):
    pass

if __name__ == '__main__':
    s = rand_state(n)
    print(tostring(s))
    print(h(s))
    actions_ = actions(s)
    print(actions_)
