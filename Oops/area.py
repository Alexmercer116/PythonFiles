class Rectangle :

    def area(self,l,b):
        
        print(l*b)

    def peri(self,l,b):

        print(2*(l+b))

class Circle :

    from math import pi,trunc
    def area(self,r):
        
        print(self.pi*r**2)

    def circum(self,r):

        print(float(2*self.pi*r))
        
class Square :

    def area(self,l):
        
        print(l**2)
    def peri(self,l):

        print(2*l)


rect = Rectangle()

circ = Circle()

sq = Square()


rect.area(20,30)
rect.peri(10,12)

rect.area(10,14)
circ.area(5)

