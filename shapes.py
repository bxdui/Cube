import turtle, random

class SuperShape:
    def __init__(self, sides, thickness, fourcolor, color, size):
        turtle.colormode(255)
        self.sides = sides
        self.thickness = thickness
        self.color = color
        self.size = size
        self.fourcolor = fourcolor
        turtle.color(self.color)
        turtle.width(self.thickness)

    def draw(self):
        for i in range(self.sides):
            if self.fourcolor == True:
                for i in range(8):
                    turtle.color((random.randint(1,255), random.randint(1,255), random.randint(1,255)))
                    turtle.forward(self.size/8)
            else:
                turtle.forward(self.size)
            turtle.right(360/self.sides)

red_square = SuperShape(4, 5, False, 'red', 100)
blue_square = SuperShape(4, 5, False, 'blue', 100)
rainbow_square = SuperShape(4, 5, True, 'blue', 100)
rainbow_triangle = SuperShape(3, 5, True, 'blue', 100)
rainbow_pentagon = SuperShape(5, 5, True, 'blue', 100)
rainbow_hexagon = SuperShape(6, 5, True, 'blue', 100)
rainbow_septagon = SuperShape(7, 5, True, 'blue', 100)
rainbow_octagon = SuperShape(8, 5, True, 'blue', 100)

rainbow_triangle.draw()
