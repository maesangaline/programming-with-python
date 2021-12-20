# Marcie Sangaline
# CPT 156 Programming with Python
# Chapter 5, Exercise 21

# Imports the random function
import random

# Create a game of rock, paper, scissors that the computer chooses their option
def rpsGame():
    n = random.randrange(1, 4)
    com = ''
    if n == 1:
        com = 'rock'
    elif n == 2:
        com = 'paper'
    else:
        com = 'scissors'
    player = input('\'rock\', \'paper\' or ' '\'scissors\': ')
    print(com)
    return com, player

# Creates the rules of the game
def rules(com, player):
    # If the computer and player make the same selection, the game restart
    while com == player:
        com, player = rpsGame()
    # If the computer and player make different selections
    # these are the rules to determine the winner
    # Rock beats scissors. Scissors beats paper. Paper beats rock.
    else:
        if com == 'rock' and player == 'scissors':
            print('The computer wins')
        elif com == 'scissors' and player == 'paper':
            print('The computer wins')
        elif com == 'paper' and player == 'rock':
            print('The computer wins')
        elif com == 'paper' and player == 'scissors':
            print('You win')
        elif com == 'scissors' and player == 'rock':
            print('You win')
        elif com == 'rock' and player == 'paper':
            print('You win')

def main():
    com, player = rpsGame()
    rules(com, player)
main()
