import math as m
class Spherical:
    def __init__(self,r):
        self.r = r
        self.findArea()
        self.findVolume()
    def changeR(self,Radius):
        self.r = Radius
        self.findArea()
        self.findVolume()

    def findVolume(self):
        self.Volume = (4*m.pi*(self.r**3))/3

    def findArea(self):
        self.area = 4*m.pi*(self.r**2) 

    def __str__(self):
        return "Radius ={} Volume = {} Area = {}".format(self.r,self.Volume,self.area)

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)