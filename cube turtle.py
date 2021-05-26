import turtle

class Blocks:
    def __init__(self, color, thickness):
        self.color = color
        self.thickness = thickness
        turtle.color(self.color)
        turtle.width(self.thickness)

    def draw_square(self):
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)

    def draw_legs(self):
        ang_lst1 = [45, 135, 225]
        ang_lst2 = [45, 315, 0]
        n = 0
        for i in range(3):
            turtle.forward(100)
            turtle.right(ang_lst1[n])
            turtle.forward(56)
            turtle.right(ang_lst2[n])
            n += 1

    def draw(self):
        for i in range(2):
            self.draw_square()
            turtle.goto(-40, 40)
        self.draw_legs()

red_block = Blocks('red', 5)

red_block.draw()