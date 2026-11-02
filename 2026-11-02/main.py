from PropFormula import *

"""
CSP
1. graph coloring
   colors = {r, g}

               (A)
                |
               (C)-(B)
                |
               (D)

2. knight's tour

variable   - strings
domain     - list
constraint - 
  propositional formula
    proposition with variables, substitute values into variables,
    you get a boolean value
assignment is (var, value)
    example for A=1, ('A', 1)
assignments is list of assignment values as above
"""

class CSP:
    def __init__(self, Vars, Doms, Cons):
        self.Vars = Vars
        self.Doms = Doms
        self.Cons = Cons
    def __str__(self):
        s = ""
        for k, v in self.Cons.items():
            s += '          %s: %s\n' % (k, v)
        return '''<CSP
    Vars: %s
    Doms: %s
    Cons:
%s>''' % (self.Vars, self.Doms, s)
    
'''
               (A)
                |
               (C)-(B)
                |
               (D)

A != C
B != C
C != D
find assignment A=0, B=0, C=1, D=0, i.e., [('A',0), ('B',0), ...]
'''

def bt(csp, assignments):
    # base case: check if assignments is already complete
    if len(csp.Vars) == 0:
        return True
    
    # recursive case
    # 1. pick a variable V in csp.Vars
    # 2. pick a value v in csp.Doms[V]
    # 3. Get assignment V=v, i.e., (V, v). put into assignments, call bt
    #    If True, return True
    #    Else, unremove (V, v) 
    #    Loop 2-3 and try another value for v
    # 4. Return False

    '''
    V = csp.Vars[0]
    for v in csp.Doms[V]:
        # Choose V=v assignment
        # 1. create (infer) new CSP object
        # 2. create new assignments
        Vars = csp.Vars[:]; Vars.remove(V)
        Doms = {k:v for k,v in csp.Doms.items()}        
        csp0 = CSP(Vars, Doms, Cons)
        assignments.append((V, v))
        flag = bt(csp0, assignments)
        if flag: return True
        assignments.pop()
    return False
    '''

A, B, C, D = 'A', 'B', 'C', 'D'

Vars = [A, B, C, D]
Doms = {}
Doms[A] = {0, 1}
Doms[B] = {0, 1}
Doms[C] = {0, 1}
Doms[D] = {0, 1}
Cons = {}
Cons[(A, C)] = PropFormula("A != C")
Cons[(B, C)] = PropFormula("B != C")
Cons[(C, D)] = PropFormula("C != D")
csp = CSP(Vars, Doms, Cons)
assignment = []

var = 'A'
val = 0
Vars = csp.Vars[:]
Vars.remove(var)
print("Vars:", Vars)
import copy
Doms = copy.deepcopy(csp.Doms)
del Doms[var]
print("Doms:", Doms)

Cons = copy.deepcopy(csp.Cons)
d = {}
for k in Cons:
    if var in k:
        P = Cons[k]             # P = A != C
        P = P.subst(var, val) # P = 0 != C
        xs = list(k)
        xs.remove(var)
        xs = tuple(xs)
        d[xs] = P
    else:
        d[k] = Cons[k]
Cons = d

for k,v in Cons.items():
    print(k, v)

#csp1 = CSP(Vars, Doms, Cons)
#CSP0 = CSP(Vars=Vars,
#           Doms=Doms,
#           Cons=Cons)
#print(CSP0)

