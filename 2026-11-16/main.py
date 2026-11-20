import random; random.seed()
import math

class Neuron:
    def __init__(self, activation, ws=None, n=None):
        #assert isinstance(activation, Activation)
        self.activation = activation
        if ws == None:
            self.n = n
            self.ws = [random.random() for _ in range(n + 1)]
        else:
            self.n = len(ws)
            self.ws = ws
    def __str__(self):
        return "<Neuron %s %s>" % (self.activation, self.ws)
    def __call__(self, xs):
        ws = self.ws
        A = self.activation
        xs = [1.0] + xs
        z = sum(w * x for (w, x) in zip(ws, xs))
        return A(z)
    
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
        elif z > self.alpha: return 1.0
        else: return None # avoid the midpoint
    def __str__(self):
        return "Threshold(alpha=%s)" % self.alpha

#def NeuralLayer:
#    def __init__(self, Ns):
#        self.Ns = Ns
#    def __call__(self, xs):
#        xs = [1] + xs
#        outputs = [N(xs) for N in self.Ns]
#        return outputs


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
    print(N)
    xs = [0, 0]
    print("N(xs):", N(xs))

    def weights(n=10):
        return [float(_) / n for _ in [(x - n) for x in list(range(0, 2 * n))]] + [1.0]

    def brute_force_training(N, training):
        num_weights = len(N.ws) 
        for w0 in weights():
            for w1 in weights():
                for w2 in weights():
                    ws = [w0, w1, w2]
                    print(ws)
                    N.ws = ws
                    found = True
                    for t in training:
                        inputs, correct = t
                        output = N(inputs)
                        print(inputs, output, correct, output == correct)
                        if output != correct:
                            found = False
                            break
                    if found: break
                if found: break
            if found: break
        if found:
            return N
        else:
            print("ERROR: NOT FOUND")
            return None

    # OR GATE
    training = [([0,0],0),
                ([0,1],1),
                ([1,0],1),
                ([1,1],1),
                ]
    N = Neuron(activation=T, n=2)
    N = brute_force_training(N, training)
    print("our OR gate as neuron:", N)
    N_OR = N # keep or gate

    # AND GATE
    training = [([0,0],0),
                ([0,1],0),
                ([1,0],0),
                ([1,1],1),
                ]
    N = Neuron(activation=T, n=2)
    N = brute_force_training(N, training)
    print("our AND gate as neuron:", N)
    N_AND = N # keep or gate

    # GATE for ~x1 AND x2
    training = [([0,0],0),
                ([0,1],1),
                ([1,0],0),
                ([1,1],0),
                ]
    N = Neuron(activation=T, n=2)
    N = brute_force_training(N, training)
    print("Gate(x1, x2) = ~x1 * x2 as neuron:", N)
    N1 = N # keep our gate

    # GATE for x1 AND ~x2
    training = [([0,0],0),
                ([0,1],0),
                ([1,0],1),
                ([1,1],0),
                ]
    N = Neuron(activation=T, n=2)
    N = brute_force_training(N, training)
    print("Gate(x1, x2) = x1 * ~x2 as neuron:", N)
    N2 = N # keep our gate

