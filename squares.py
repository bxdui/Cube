import turtle, random

class SuperSquare:
    def __init__(self, thickness, fourcolor, color, size):
        turtle.colormode(255)
        self.thickness = thickness
        self.color = color
        self.size = size
        self.fourcolor = fourcolor
        turtle.color(self.color)
        turtle.width(self.thickness)

    def drawsquare(self):
        for i in range(4):
            if self.fourcolor == True:
                for i in range(8):
                    turtle.color((random.randint(1,255), random.randint(1,255), random.randint(1,255)))
                    turtle.forward(self.size/8)
            else:
                turtle.forward(self.size)
            turtle.right(90)

red_square = SuperSquare(5, False, 'red', 100)
blue_square = SuperSquare(5, False, 'blue', 100)
rainbow_square = SuperSquare(5, True, 'blue', 100)

rainbow_square.drawsquare()
