class methods:
    def __init__(self):
        self.s=""
    def getstring(self):
        self.s = input()
    def printstring(self):
        print(self.s.upper())
        
strmet = methods()
strmet.getstring()
strmet.printstring()