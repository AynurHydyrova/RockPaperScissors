import random

moves = ['rock', 'paper', 'scissors']


class Player():
    def move(self):
        return 'rock'
 
    def learn(self, my_move, their_move):
        self.my_move = their_move
        self.their_move = their_move
 

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return (random.choice(moves))
 


class HumanPlayer(Player):
    def move(self):
        while True:
            user = input("Please choose Rock, Paper or Scissors? ")
            if user.lower() not in moves:
                print("Invalid input choose Rock, Paper or Scissors")
            else:
                return(user.lower())


class ReflectPlayer(Player):
    def move(self):
        if their_move=="rock":
            return "rock"
        elif their_move == "paper":
            return "paper"
        elif their_move == "scissors":
            return "scissors"
        else:
            return "rock"
 
class CyclePlayer(Player):
    def move(self):
        if self.my_move=="rock":
            return "paper"
        elif my_move=="paper":
            return "scissors"
        elif my_move=="scissors":
            return "rock"
        else:
            return "rock"
            
 
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1score = 0
        self.p2score = 0
 

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print ("Human: {move1} Machine: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.p1.beats(move1, move2)
        if beats(move1, move2) is True:
            self.p1score += 1
            print("Human won")
        elif beats(move2, move1) is True:
            self.p2score += 1
            print("Machine wins!")
        elif move1 == move2:
            print("nobody wins")
        print(self.p1score, self.p2score)


    def play_game(self):
        print("Let the game begin")
        selection = int(input("Select rounds you want play? "))
        for round in range(selection):
            print("Round {round}:")
            self.play_round()
        print("The result is {self.p1score} to {self.p2score}")
        if self.p1score > self.p2score:
            print("Human wins")
        elif self.p1score < self.p2score:
            print("Machine wins")
        else:
            print("we have tie")
 
if __name__ == '__main__':
     game = Game(HumanPlayer(), CyclePlayer())
     game.play_game()
