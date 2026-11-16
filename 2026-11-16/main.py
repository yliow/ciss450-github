import random; random.seed()
import math

class Neuron:
    def __init__(self, activation, ws=None, n=None):
        self.activation = activation
        if ws == None:
            self.n = n
            self.ws = [random.random() for _ in range(n + 1)]
        else:
            self.n = len(ws)
            self.ws = ws
    def __str__(self):
        return
    
class Activation:
    def __init__(self):
        pass
    def __call__(self, x):
        pass
    def __str__(self):
        pass
    
class Sigmoid(Activation):
    def __init__(self):
        Activation.__init__(self)
    def __call__(self, z):
        return 1.0 / (1.0 + math.exp(-z))
    def __str__(self):
        return "Sigmoid"
    
class Threshold(Activation):
    def __init__(self, alpha):
        Activation.__init__(self)
        self.alpha = alpha
    def __call__(self, z):
        if z < self.alpha: return 0.0
        else: return 1.0
    def __str__(self):
        return "Threshold(alpha=%s)" % self.alpha
    
if __name__ == '__main__':
    S = Sigmoid()
    print(S)
    print("Sigmoid(0) =", S(0))
    print("Sigmoid(99) =", S(99))
    print("Sigmoid(-99) =", S(-99))
    T = Threshold(0.5)
    print(T)
    print("Threshold(0.3) =", T(0.3))
    print("Threshold(0.6) =", T(0.6))
    N = Neuron(activation=T, n=2)
