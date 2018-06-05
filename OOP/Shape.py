class Shape:
    def draw(self):
        self.drawSelf()

    def shapePrint(self):
        print("printed shape")

class Point(Shape):
    def drawSelf(self):
        print("draw point")


class Circle(Point):
    def drawSelf(self):
        print("draw Circle")


shape = Point()
shape.draw()


class A:
    def __init__(self):
        self.name="A"

class B:
    def __init__(self):
        self.name="B"


class AB(B,A):
    def Info(self):
        print(\
            self.name)
ab = AB()
ab.Info()
print()