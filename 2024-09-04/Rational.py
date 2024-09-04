class Rational:

    num_of_objects = 0
    
    def __init__(self, n, d):
        self.__n = n
        self.__d = d
        Rational.num_of_objects += 1
        
    def __str__(self):
        return "%s/%s" % (self.__n, self.__d)
    def __repr__(self):
        return "<Rational %s n:%s, d:%s>" % (id(self),
                                             self.__n,
                                             self.__d)
    def __add__(self, r):
        n = self.__n * r.__d + self.__d * r.__n
        d = self.__d * r.__d
        return Rational(n, d)

    #@staticmethod
    #def f():
    #    asdasdsaadsad
