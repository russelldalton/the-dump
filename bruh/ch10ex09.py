import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4 * math.pi * self.radius ** 2 

    def volume(self):
        return 4.0/3.0 * math.pi * self.radius ** 3

def main():
    r = float(input('what is the radius '))
    mySphere = Sphere(r)
    print("the surface area is {:0.2f} square units".format(mySphere.surfaceArea()))
    print("the volume is {:0.2f} cubic units".format(mySphere.volume()))
if __name__ == '__main__':
    main()
