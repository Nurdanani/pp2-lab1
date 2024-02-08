class Shape(object):
     def __init__(self):
         pass 
     def area(self):
         return 0
class rectangle(Shape):
    def __init__(self, length , width):
        Shape.__init__(self)
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
aSq= rectangle(4,7)
print(aSq.area())
    
    