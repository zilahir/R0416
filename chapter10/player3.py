
class Player:
    """
        Player-class: stores data on team colors and points
    """
    def __init__(self):
        self.teamColor = input("What color do I get?: ")
        self.points = 0

    def tellscore(self):
        print(f"I am {self.teamColor}, we have {self.points} points!")
    
    def goal(self):
        self.points += 1

def main():
    player1 = Player()
    player2 = Player()
    player1.goal()
    player1.goal()
    player2.goal()

    player1.tellscore()
    player2.tellscore()


if __name__ == "__main__":
    main()