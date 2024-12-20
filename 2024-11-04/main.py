import random; random.seed()

n = 16

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
    #print(points)
    s = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            p0 = points[i]
            p1 = points[j]
            s += int(isattacking(p0, p1))
            #print((i, j), p0, p1, isattacking(p0, p1), s)
    return s

def actions(m):
    '''
    return [((r, c), +1), ((r, c), -1),....]
    '''
    n = len(m)
    ret = []
    for r, row in enumerate(m):
        for c, v in enumerate(row):
            if v == 'Q':
                point = (r, c)
                if c < n - 1:
                    ret.append((point, +1))
                if c > 0:
                    ret.append((point, -1))
                break
    return ret

import copy

def solve():
    """ solve using SA """

    m = rand_state(n)
    best_h = h(m)
    #best_options = [m] # (a, b) = (action, state)
    printboard(m)
    print(best_h)
    #input("? ")

    # hc ... go over all succ and pick the best

    t = 0
    a = 1.0
    max_t = 1000
    while 1:

        """ hc hill climbing
        improve = False
        for action in actions(m):
            (r, c), dc = action
            m0 = copy.deepcopy(m)
            m0[r][c] = ' '
            m0[r][c + dc] = 'Q'
            obj0 = h(m0)
            if obj0 == best_h:
                best_options.append(m0)
            elif obj0 < best_h:
                improve = True
                best_h = obj0
                best_options = [m0]
            else:
                pass # dont consider a bad option

        if not improve:
            break
        else:
            m = random.choice(best_options)
            printboard(m)
            print(best_h)
        """

        # simulated annealing
        actions_ = actions(m)
        if len(actions_) == 0:
            break
        action = random.choice(actions_)
        m0 = action
        (r, c), dc = action
        m0 = copy.deepcopy(m)
        m0[r][c] = ' '
        m0[r][c + dc] = 'Q'
        obj0 = h(m0)

        # now we have m,best_h and m0,obj0
        if obj0 < best_h:
            m = m0
            best_h = obj0
        else:
            x = random.uniform(0.0, 1.0)
            if x < a:
                m = m0
                best_h = obj0

        printboard(m)
        print(best_h)
        
        input("? ")
        t += 1
        if t >= max_t: break
        a = a / t
        
        '''
        # TEST
        action = random.choice(as_)
        print("action:", action)
        (r, c), dc = action
        m0 = copy.deepcopy(m)
        m0[r][c] = ' '
        m0[r][c + dc] = 'Q'
        obj0 = h(m0)
        printboard(m0)
        print(obj0)
        break
        '''
        
    return m

if __name__ == '__main__':
     m = solve()
