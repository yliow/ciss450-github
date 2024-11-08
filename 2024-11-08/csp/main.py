"""
CSP
variables X1, X2, X3, ...
domains D1, D2, D3, ...
constraints C1, C2, C3, ...
"""
class CSP:
    def __init__(self,
                 vars,    # example: ["X1", "X2, "X3"]
                 domains, # example: {"X1":['r', 'g', 'b'],
                          #           "X2":['r', 'g', 'b'],
                          #           "X3":['r', 'g', 'b']}
                 constraints, # example: ["X1 != X2", "X1 != X3"]
    ):
        self.vars = vars
        self.domains = domains
        self.constraints = constraints

''' use graph coloring problem
X ------ Y
|
|
|
|
Z
'''
X = 'X'
Y = 'Y'
Z = 'Z'
r = 'r'
g = 'g'
b = 'b'

csp = CSP(vars=[X, Y, Z],
          domains={X:[r, g, b],
                   Y:[r, g, b],
                   Z:[r, g, b]},
          constraints = {("X", "Y"): "X != Y",
                         ("X", "Z"): "X != Z"}
)
assignment = [(X, r)]

vars2 = [_ for _ in csp.vars if _ != assignment[0][0]]
print("vars2:", vars2)

domains2 = {}
var0 = assignment[0][0]
for var1 in vars2:
    print("(var0, var1):", (var0, var1))
    if (var0, var1) in csp.constraints.keys():
        c = csp.constraints[(var0, var1))
        print("c:", c)
        #domains2[var1] = {}
        
print("domains2:", domains2)

asd
constraints2 = None
csp2 = CSP(vars = vars2,
           domains = domains2,
           constaints = contraints2)
          
