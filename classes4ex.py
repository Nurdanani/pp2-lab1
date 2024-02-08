class point():
    def __init__(self, x, y):
        self.x= x
        self.y = y
        
    def show(self):
        print(f'({self.x}, {self.y})')
        
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
        
    def dist(self , other):
        distance =((self.x - other.x)**2+(self.y-other.y)**2)**0.5
        return distance
    
point1 = point(2, 3)
point2 = point(5, 7)

point1.show()
point1.move(8, 11)
print(point1.dist(point2))