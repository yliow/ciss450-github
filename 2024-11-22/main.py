"""
A logic library for CSP and logic agents

X = PropVar("X")
Y = PropVar("Y")
Z = PropVar("Z")
print(X, Y, Z)

e = X and Y <-- logic of X, Y
notation: e = AND(X, Y)
print(e) ----> "X & Y"

e1 = SUBST(e, [(X, TRUE)])
print(e1) -----> "TRUE & Y"

e2 = SIMPLIFY(e1)
print(e2) ------> "Y" (in dm225: X and TRUE = X, TRUE & TRUE = TRUE)

Only propositional logic.
No predicate logic.
"""

TRUE = 1
FALSE = 0

class PropVar:
    """
    Each propositional variable must be uniquely defined
    by their name.
    """
    def __init__(self, name='[NONE]'):
        self.name = name
    def __str__(self):
        return self.name

class AND:
    def __init__(self, X, Y):
        self.left = X
        self.right = Y
    def __str__(self):
        return "(%s & %s)" % (self.left, self.right)

class OR:
    def __init__(self, X, Y):
        self.left = X
        self.right = Y
    def __str__(self):
        return "(%s | %s)" % (self.left, self.right)

def SUBST(e, assignment):
    """
    e = X & Y, X=TRUE ---> return TRUE & Y

    SUBST(X & Y, X=TRUE)
    = SUBST(AND(X, Y), X=TRUE)
    = AND(SUBST(X, X=TRUE), SUBST(Y, X=TRUE))
    """
    if isinstance(e, PropVar):
        for var, val in assignment:
            if e.name == var.name: # <-- WARNING: 
                return val
    elif isinstance(e, AND):
        left = SUBST(e.left, assignment)
        right = SUBST(e.right, assignment)
        return AND(left, right)
    elif isinstance(e, OR):
        left = SUBST(e.left, assignment)
        right = SUBST(e.right, assignment)
        return OR(left, right)
    
if __name__ == '__main__':
    X = PropVar("X")
    Y = PropVar("Y")
    Z = PropVar("Z")
    print(X, Y, Z)
    e = AND(X, Y)
    print(e)
    f = AND(e, Z) # (X & Y) & Z
    print(f)
    g = OR(e, Z)
    print(g)
    e1 = SUBST(e, [(X, TRUE)])
    print("e1:", e1)
