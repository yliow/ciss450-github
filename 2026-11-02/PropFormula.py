class PropFormula:
    def __init__(self, s):
        self.s = s
    def __str__(self):
        return "<PropFormula %s>" % self.s
    def subst(self, var, val):
        return PropFormula(self.s.replace(var, str(val)))
    def eval(self):
        try: return eval(self.s)
        except: return None
    
if __name__ == '__main__':
    P = PropFormula("A != C")
    print(P)
    Q = P.subst('A', 0) # Q is a PropFormula "0 != C"
    print(Q)
    R = Q.subst('C', 1)
    print(R)
    print(R.eval())
    print(Q)
    print(Q.eval())
