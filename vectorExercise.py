#Exercise: make a vector class that supports appending, addition, subtraction, indexing, magnitude, and dot products
#Skills: Classes, operator overloading

class vector:
    def __init__(self, *args):
        if len(args) == 0:
            self.elems = []
        elif len(args) == 1:
            try:
                self.elems = list(args[0])
            except:
                self.elems = list(args)
        else:
            self.elems = list(args)

    def __getitem__(self, key):
        return self.elems[key]

    def __setitem__(self, key, val):
        self.elems[key] = val

    def append(self, val):
        self.elems.append(val)

    def __len__(self):
        return len(self.elems)

    def __add__(self, other):
        if len(self) == len(other):
            return vector([a+b for a, b in zip(self, other)])
        else:
            raise IndexError('Need vectors of same length')

    def __neg__(self):
        return vector([-a for a in self.elems])

    def __sub__(self, other):
        try:
            return self + -other
        except:
            if len(self) == len(other):
                return vector([a-b for a, b in zip(self, other)])
            else:
                raise IndexError('Need vectors of same length')

    def __mul__(self, other):
        if len(self) == len(other):
            return sum([a*b for a, b in zip(self, other)])
        else:
            raise IndexError('Need vectors of same length')

    def __abs__(self):
        return (self*self)**0.5
    
    def __str__(self):
        commalist = ''.join([str(a) + ', ' for a in self.elems])
        return '<' + commalist[:-2] + '>'

#Bonus: make a matrix class with transpose, matrix multiplication, dimensions, and all applicable vector operations
#Skills: Inheritance
    
class matrix(vector):
    def __init__(self, *args):
        if len(args) == 0:
            self.elems = vector()
        elif len(args) == 1:
            try:
                self.elems = vector([vector(a) for a in args[0]])
            except:
                self.elems = vector()
                self.elems.append(vector(args[0]))
        else:
            self.elems = vector([vector(a) for a in args])

    def T(self):
        return matrix(zip(*self))

    def __mul__(self, other):
        return matrix([[b*a for a in other.T()] for b in self])

    def dims(self):
        return (len(self), len(self[0]))
