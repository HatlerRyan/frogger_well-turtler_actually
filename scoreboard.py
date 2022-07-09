from turtle import Turtle, Screen
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 0
        self.hideturtle()
        self.penup()

    def level_display(self):
        self.goto(-270, 250)
        self.current_level += 1
        self.clear()
        self.write(F"Level: {self.current_level}", font=FONT)

    def end_game(self):
        self.goto(0,0)
        self.write(F"GAME OVER", align="left", font=FONT)


