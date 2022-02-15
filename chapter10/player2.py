
class Player:
    def __init__(self, teamColor, points):
        self.teamColor = teamColor
        self.points = points

    def tellscore(self):
        print(f"I am {self.teamColor}, we have {self.points} points!")

def main():
    player = Player("Blue", 1)
    player.tellscore()


if __name__ == "__main__":
    main()