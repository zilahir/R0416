
class Player:
    def __init__(self, teamColor, points):
        self.teamColor = teamColor
        self.points = points

    def getInfo(self):
        print(f"The {self.teamColor} contender has {self.points} points!")

def main():
    player = Player("Blue", 300)
    player.getInfo()


if __name__ == "__main__":
    main()