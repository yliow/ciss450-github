"""
simulation of ab pruning
"""

def successors(s):
    d = {"s1": [("a1", "s2"), ("a2", "s3"), ("a3", "s4")]
         "s2": [("a4", "s5"), ("a5", "s6"), ("a6", "s7")],
         "s3": [("a7", "s8"), ("a8", "s9"), ("a9", "s10")],
         "s4": [("a10", "s11"), ("a11", "s12"), ("a12", "s13")]}
    d1 = dict([("s%s" % _, []) for _ in range(5, 14)])
    print(d1)

successors("s1")
