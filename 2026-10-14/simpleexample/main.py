"""
Solve

X + Y < Z

for X in {1, 2, 3}
    Y in {1, 2, 3}
    Z in {1, 2, 3}
"""

class CSP:
    def __init__(self,
                 Vars,
                 Doms,
                 C):
        self.Vars = Vars
        self.Doms = Doms
        self.C = C
    def __str__(self):
        return """<CSP
  Vars: %s
  Doms: %s
  C: %s
>
""" % (self.Vars, self.Doms, self.C)

def substitute(prop, var, value):
    ret = prop.replace(var, value)
    return ret

def bt_solve(csp, assignment):
    """
    return a consistent and complete assignment (if any)
    """
    pick a var V
    for v in domain of V:    
        add (V, v) to assignment, i.e., assignment = assignment + (V, v)
        call solve(csp, assignemtn)
    
    
if __name__ == '__main__':
    csp = CSP(Vars = ['X', 'Y', 'Z'],
              Doms = {'X':[1, 2, 3], 'Y':[1, 2, 3], 'Z':[1, 2, 3]},
              C = {('X', 'Y', 'Z'): "X + Y < Z"})
    print(csp)

    '''
    prop = "X + Y < Z"
    prop = substitute(prop, 'X', '1')
    print(prop)
    '''
    solve(csp)
