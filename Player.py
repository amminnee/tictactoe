class player():
    def __init__(self, n):
        self.name = "player {}".format(n+1)
        self.score = 0
        if n == 0:
            self.fill = "X"
        else:
            self.fill = "O"

    def updateName(self, name):
        self.name = name

    def updateScore(self):
        self.score += 1

    def resetScore(self):
        self.score = 0
        