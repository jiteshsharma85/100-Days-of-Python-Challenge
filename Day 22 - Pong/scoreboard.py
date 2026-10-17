from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.left_score = 0
        self.right_score = 0
        self.update_score()


    # Redraws the score display on screen
    def update_score(self):
        self.write(f"{self.left_score}  |  {self.right_score}", align= "center", font=("Courier", 20, "normal"))

    # Increments the left player's score
    def left_add(self):
        self.clear()
        self.left_score += 1
        self.update_score()



    # Increments the right player's score
    def right_add(self):
        self.clear()
        self.right_score += 1
        self.update_score()
