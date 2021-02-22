from models import *
import exceptions
from settings import player_lives


if __name__ == '__main__':

    def play():
        player_name = Player(str(input('Please, enter player name: \n')),
                             lives=int(input('Choose the number of lives:\n'
                                             '3 lives - is a easy level\n'
                                             '2 lives - is a intermediate level\n'
                                             '1 lives - is a hard level\n')))

        try:
            player_lives(player_name.lives)
        except IncorrectPlayerLives:
            print('Choose the correct level')
            player_lives(player_name.lives)

        # you = Player(player_name)
        # enemy = Enemy(level)
        enemy = Enemy(1, 1)

        time_to_play = input('Enter "start" to start the game: \n')

        if time_to_play == "start":
            while True:
                try:
                    player_name.attack(enemy)
                    player_name.defence(enemy)
                    if player_name.attack(enemy) == "You attacked successfully":
                        enemy.decrease_lives()
                except exceptions.EnemyDown:
                    player_name.score += 5
                    print('Your score: {} '.format(player_name.score))
                    print('\n\nLEVEL UP!\n\n')
                    enemy.level += 1
                    enemy.lives = enemy.level
                    print('Enemy: {} - level, {} - lives'.format(enemy.level, enemy.lives))


    try:
        play()
    except exceptions.GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye!')

