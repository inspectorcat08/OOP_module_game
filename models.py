from exceptions import *
from settings import player_lives
from random import randint
from datetime import datetime



class Enemy:

    def __init__(self, lives, level = 1):
        self.level = level
        self.lives = lives

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown

class Player:

    score = 0
    allowed_attacks = (1, 2 ,3)

    def __init__(self,  name, lives):
        self.player_name = name
        self.lives = lives


    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            print("You have: {} scores".format(self.score))
            scores = open('scores.txt', 'a+')
            scores.write("Player {}: {} points - {}\n".format(self.player_name, self.score, datetime.utcnow()))
            scores.close()
            raise GameOver


    @staticmethod
    def fight(attack, defense):
        if (attack==1 and defense==2) \
                or (attack==2 and defense==3)\
                or (attack==3 and defense==1):
            return 1
        elif attack==defense:
            return 0
        else:
            return -1

    def attack(self, enemy_obj):
        self.allowed_attacks = int(input("Select an attacking character:\n1 - Wizard  2 - Warrior  3 - Robber\n"))
        hit = self.fight(self.allowed_attacks, enemy_obj.select_attack())
        if hit == 0:
            print("It's a draw!\n")
        elif hit == 1:
            self.score += 1
            print("You attacked successfully!\n")
            enemy_obj.decrease_lives()
        elif hit == -1:
            print("You missed!\n")


    def defence(self, enemy_obj):
        self.allowed_attacks = int(input("Select a defending character: \n1 - Wizard  2 - Warrior  3 - Robber\n"))
        hit = self.fight(enemy_obj.select_attack(), self.allowed_attacks)
        if hit == 0:
            print("It's a draw!\n")
        elif hit == 1:
            self.decrease_lives()
            print("Enemy attacked successfully!\n")
        elif hit == -1:
            print("Enemy missed!\n")



