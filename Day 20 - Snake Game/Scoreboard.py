from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 26, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            value = int(file.read())
        self.high_score = value
        self.color("white")
        self.penup()
        self.goto((0, 265))
        self.hideturtle()
        self.update_score()

    # Clears and redraws the score on screen
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    # Saves a new high score to file if current score beats it, then resets
    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_is_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align= ALIGNMENT, font=FONT)


    # Increments the score by 1 and updates the display
    def adding_score(self):

        self.score += 1
        self.update_score()


