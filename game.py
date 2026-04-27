import random



class Player:
    def __init__(self):
        self.position = 1

class Game:
    snake_amount = 5
    ladder_amount = 5

    def __init__(self):
        self.snakes = self.generateSnakes()
        self.ladders = self.generateLadders()
        self.p1 = Player()
        self.p2 = Player()
        self.winner = None

    def generateSnakes(self):
        snakes = {}

        for i in range(self.snake_amount):
            upper = random.randint(2, 99)
            lower = upper - random.randint(1, upper)

            snakes[upper] = lower

        return snakes
    
    def generateLadders(self):
        ladders = {}
        for i in range(self.ladder_amount):
            lower = random.randint(1, 98)
            upper = lower + random.randint(1, (99 - lower)) # 99 as 100 can cause the player to instawin 

            ladders[lower] = upper

        return ladders

    def takeTurn(self, player):
        input(f'You are at position {player.position}. Press enter to roll.')
        roll = random.randint(1, 6)
        print(f'You rolled {roll}!')

        if player.position + roll > 100:
            print(f'You surpassed 100 and made it to {player.position + roll}! You will be reset back to {player.position}.')
            return None
        
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
        for row in range(9, -1, -1):
            full_row = ""
            for col in range(10):
                if row % 2 != 0: # Backward
                    num = row * 10 + (9 - col) + 1
                else: # Forward
                    num = row * 10 + col + 1
                
                if num in self.snakes:
                    display = f"s->{self.snakes[num]}"
                elif num in self.ladders:
                    display = f"l->{self.ladders[num]}"
                else:
                    display = str(num)
                
                full_row += display + " " * (8 - len(display))
            print(full_row)


def main():
    game = Game()

    while game.winner == None:
        game.takeTurn(game.p1)
        game.takeTurn(game.p2)



main()