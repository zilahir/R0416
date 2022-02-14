import random

class Game:
    def __init__(self, players):
        self.players = players
        self.choices = ["Foot", "Nuke", "Cockroach"]
        self.winners = []
        self.results = {
            "draw": 0,
            "player1": 0,
            "player2": 0
        }
    
    def getChooseByNumber(self, number):
        return self.choices[number - 1]
    
    def getChooseByText(self, text):
        return self.choices.index(text)
    
    def mod(self, a, b,):
        c = a % b;
        if c < 0:
            return c + b
        else: return c
    
    def setWinner(self, winner):
        self.results[winner] = self.results[winner] + 1

    def decideWinner(self):
        player1Choices = self.players[0].getChoices()
        player2Choices = self.players[1].getChoices()
        player1LastChoice = player1Choices[len(player1Choices) - 1]
        player2LastChoice = player2Choices[len(player2Choices) - 1]
        player1ChoiceIndex = self.choices.index(self.getChooseByNumber(player1LastChoice))
        player2ChoiceIndex = self.choices.index(self.getChooseByNumber(player2LastChoice))

        print (f'Player 1 {player1ChoiceIndex}')
        print (f'Player 2 {player2ChoiceIndex}')
        if (player1ChoiceIndex == player2ChoiceIndex):
            return self.setWinner('draw')
        if self.mod(player1ChoiceIndex - player2ChoiceIndex, len(self.choices)) < len(self.choices) / 2:
            return self.setWinner('player1')
        else:
            return self.setWinner('player1')


class Player:
    def __init__(self, playerName):
        self.playerName = playerName
        self.choiceOptions = [1, 2, 3]
        self.choices = []

    def makeChoice(self, newChoice ):
        self.choices.append(int(newChoice))
        return newChoice

    def getMe(self):
        return self.playerName
    
    def getChoices(self):
        return self.choices

    def getRandomChoice(self):
        return random.choice(self.choiceOptions)

def main():
    me = Player("Me")
    computer = Player("Computer")
    players = []
    players.append(me)
    players.append(computer)
    game = Game(players)

    myInput = None
    while (myInput != "q"):
        # we are playing until quit
        for player in players:
            if (player.getMe() == 'Me'):
                myChoice = input("Foot, Nuke or Cockroach? (Quit ends): ")
                if (myChoice != "q"): #only I can quit the game, computer can't
                    # print (f"You choose: {game.getChooseByNumber(int(myChoice))}")
                    # my solution would be simpler by entering number
                    # but that what not what was asked in the assignment
                    print (f"You choose: {myChoice}")
                    choiceNumber = game.getChooseByText(myChoice)
                    player.makeChoice(choiceNumber)
                else:
                    return 0
            else:
                randomChoice = player.getRandomChoice()
                print (f"Computer choose: {game.getChooseByNumber(int(randomChoice))}")
                player.makeChoice(randomChoice)
        game.decideWinner()

    if (myInput == "q"):
        return 0


if __name__ == "__main__":
    main()