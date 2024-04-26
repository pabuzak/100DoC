from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(y=275, x=0)
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 16, 'bold'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.create_scoreboard()
        


