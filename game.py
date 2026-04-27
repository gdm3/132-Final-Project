import random

class Player:
    def __init__(self):
        self.position = 1
        self.name = None # names are set with Game.setName

class Game:

    def __init__(self):
        self.getSnakeLadderAmount() # ask for snakes+ladder amount before we generate them
        self.snakes = self.generateSnakes()
        self.ladders = self.generateLadders()
        self.p1 = Player()
        self.p2 = Player()
        self.winner = None


    def getSnakeLadderAmount(self): 
        snake_amount = 0
        ladder_amount = 0

        while snake_amount <= 0 or snake_amount >= 30: # account for too many/not enough snakes, plus non-numerical answers
            try:
                snake_amount = int(input('Please enter the number of snakes to be added: '))
                if snake_amount >= 30 or snake_amount <= 0:
                    print('Snake count must be greater than 30 and less than 0.')
            except ValueError:
                print('Please enter a valid number.')
        while ladder_amount <= 0 or ladder_amount >= 30:
            try:
                ladder_amount = int(input('Please enter the number of ladders to be added: '))
                if ladder_amount >= 30 or ladder_amount <= 0:
                    print('Ladder count must be greater than 30 and less than 0.')
            except ValueError:
                print('Please enter a valid number')

        self.snake_amount = snake_amount
        self.ladder_amount = ladder_amount
        

    def setName(self, player, name):
        player.name = name

    def generateSnakes(self): 
        snakes = {}

        for i in range(self.snake_amount):
            upper = random.randint(2, 99)
            lower = upper - random.randint(1, upper) # snakes actually go somewhere, and not off the board

            snakes[upper] = lower

        return snakes
    
    def generateLadders(self):
        ladders = {}
        for i in range(self.ladder_amount):
            lower = random.randint(1, 98)
            upper = lower + random.randint(1, (99 - lower)) # 99 as 100 can cause the player to instawin, which I dont want.

            ladders[lower] = upper

        return ladders

    def takeTurn(self, player):
        input(f'{player.name}, it is your turn. You are at position {player.position}. Press enter to roll.')
        roll = random.randint(1, 6)
        print(f'You rolled {roll}!')

        if player.position + roll > 100:
            print(f'You surpassed 100 and made it to {player.position + roll}! You will be reset back to {player.position}.')
            return # return early, so we dont actually add the roll to the position
        
        player.position += roll

        if player.position in self.snakes:
            new_position = self.snakes[player.position]
            print(f'You fell down a snake from {player.position} to {new_position}!')
            player.position = new_position
        
        elif player.position in self.ladders: # players can only use one snake/ladder per turn jsut in case they chain
            new_position = self.ladders[player.position]
            print(f'You traveled up a ladder from {player.position} to {new_position}!')
            player.position = new_position

        if player.position == 100:
            print('Congratulations! You reached 100 and won.')
            self.winner = player
            return 

        print(f'After your turn, you are at position {player.position}.')

    def displayBoard(self):
        print("Board: ")
        for row in range(9, -1, -1): # build backwards so the first line is the numbers 91-100
            full_row = ""
            for col in range(10):
                if row % 2 != 0: # odd, so go backwards
                    num = row * 10 + (9 - col) + 1
                else: # even, so go fowards
                    num = row * 10 + col + 1
                
                if num in self.snakes:
                    display = f"s->{self.snakes[num]}"
                elif num in self.ladders:
                    display = f"l->{self.ladders[num]}"
                else:
                    display = str(num)
                
                full_row += display + " " * (8 - len(display)) # subtract off current size of display from 8 to get correct spacing
            print(full_row)


def main():
    game = Game()
    
    game.setName(game.p1, input("Please enter the name of player 1: "))
    game.setName(game.p2, input("Please enter the name of player 2: "))

    game.displayBoard()

    while game.winner == None:
        game.takeTurn(game.p1)
        if game.winner == None: # prevents bug with two turns
            game.takeTurn(game.p2)

    print(f'{game.winner.name} has won the game!')


main()