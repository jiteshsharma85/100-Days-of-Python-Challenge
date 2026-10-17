from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_score()


    # Clears and redraws the current level on screen
    def update_score(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", font=FONT)

    # Increments the level counter and updates the display
    def next_level(self):
        self.level += 1
        self.update_score()

    # Displays the GAME OVER message in the centre of the screen
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
