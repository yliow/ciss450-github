# CSP

class CSP:
    def __init__(self, Vars, Doms, Cs):
        self.Vars = Vars
        self.Doms = Doms
        self.Cs = Cs
    def __str__(self):
        return """
Vars: %s
Doms:
%s
Cs:
%s
""" % (self.Vars, self.Doms, self.Cs)
    
def constraint(i, j):
    """
    Constraint for Xi,Xj of nqueens problem.
    """
    d = {'i': i, 'j':j}
    ret = "(X%(i)s != X%(j)s) and (X%(i)s - X%(j)s != %(i)s - %(j)s) and (X%(i)s - X%(j)s != -(%(i)s - %(j)s))" % d
    return ret

n = 4
Vars = ['X0', 'X1', 'X2', 'X3']
Doms={'X0':list(range(n)),
      'X1':list(range(n)),
      'X2':list(range(n)),
      'X3':list(range(n))}

Cs = {}
for i in range(0, n):
    for j in range(i + 1, n):
        Cs[('X%s' % i, 'X%s' % j)] = constraint(i, j)

nQueensCSP = CSP(Vars=Vars,
                 Doms=Doms,
                 Cs=Cs)

print(nQueensCSP)    
