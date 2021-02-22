from exceptions import *



def player_lives(lives_player):
    if lives_player == 3:
        print('You chose an easy level')
    elif lives_player == 2:
        print('You chose the intermediate level')
    elif lives_player == 1:
        print('You chose the hard level')
    else:
        raise IncorrectPlayerLives


