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

class PropVar:
    def __init__(self, name='[NONE]'):
        self.name = name
    def __str__(self):
        return self.name

class AND:
    def __init__(self, X, Y):
        self.left = X
        self.right = Y
    def __str__(self):
        return "%s & %s" % (self.left, self.right)
    
if __name__ == '__main__':
    X = PropVar("X")
    Y = PropVar("Y")
    Z = PropVar("Z")
    print(X, Y, Z)
    e = AND(X, Y)
    print(e)
    
