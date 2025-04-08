# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:11:56 2022

@author: Thomas
"""

# Importing the classes from the other files.
import random

from custompieces import * #customtroop

from pawn import *
from joker import*
from queen import * 
from tower import *
from king import *

class Player:

    def __init__(self, name, life, money):
        """
        PARAM : - name : str
                - life : float
                - money : float
        initialise team to empty list, game and direction to None
        """
        self.name = str(name)
        self.life = float(life)
        self.money = float(money)
        self.team = []
        self.game = None
        self.direction = None

    @property
    def is_alive(self):
        """
        It returns True if the life of the object is greater than 0.
        :return: The life of the player.
        """
        return self.life > 0

    def get_hit(self, damages):
        """
        Take the damage to life
        PARAM : - damages : float
        """
        self.life = self.life - damages

    def get_troops_list(self):
        """
        It returns a list of tuples, each tuple containing the life, price, strength, name/type, design
        and class of a troop
        :return: A list of tuples.
        """
        troops = [
            # (life, price, strength, name/type, design, class)
            (5, 15, 10, "Horse","H","Fighter"),
            (10, 10, 0, "Queen", "Q", "Tax recolter"), # Time lost trying to find a reasson why nothing semmed to work before I realized that I forgot the last missing coma of this line before this comment: neraly 16 hours.
            (10, 10, 4, "King","K", "Rich"),
            (20, 15, 0, "tower","T", "Tower"),
            (4, 5, 10, "Pawn","P", "Soldier"),
            (1, 50, 100, "\x1b[37;44mJoker\x1b[0m", "J", "The impossible piece"),

        ]
        return troops

    def new_character(self):
        """
        Ask to player where add a new Character,
        check if enough money
        and create the new one
        """
        if(self.name == "AI"):
            line = random.randint(0,6);
        else :
            
            line = input(f"\n{self.name}: Which line would you place the new one (0-{self.game.nb_lines-1}) ?")
            
            i=0
            while i < 1:
                
                try:
                    line=int(line)
                    
                    if -1 < line < 7:
                        troops = self.get_troops_list()
                        askTroop = ""
                        for i in range(0, len(troops)):
                            askTroop += f"\n\t{i + 1} - {troops[i][3]} /{troops[i][5]}/ ({troops[i][4]})"
                        
                        if line != "":
                            line = int(line)
                            if(self.name == "AI"):
                                troop = random.randint(0, len(troops)-1)
                            else:
                                troop = input(
                                    f"{self.name}: Which troop do you want to place (1-{len(troops)}) ?{askTroop}\n")
                                troop = int(troop) - 1
                            if 0 <= line <= self.game.nb_lines-1 and 0 <= troop <= len(troops):
                                if self.money >= troops[troop][1]:
                                    column = 0 if self.direction == 1 else self.game.nb_columns-1
                                    if(troops[troop][5] == "Fighter"):
                                        CustomPieces(self, (line, column), troops[troop][0], troops[troop][1], troops[troop][2], troops[troop][4])
                                    if(troops[troop][5] == "Tax recolter"):
                                        Queen(self, (line, column), troops[troop][0], troops[troop][1], troops[troop][2], troops[troop][4])
                                    if(troops[troop][5] == "Rich"):
                                        Pawn(self, (line, column), troops[troop][0], troops[troop][1], troops[troop][2], troops[troop][4])
                                    if(troops[troop][5] == "tower"):
                                        Tower(self, (line, column), troops[troop][0], troops[troop][1], troops[troop][2], troops[troop][4])
                                    if(troops[troop][5] == "soldier"): 
                                        King(self, (line, column), troops[troop][0], troops[troop][1], troops[troop][2], troops[troop][4])
                                    if(troops[troop][5] == "The impossible piece"):
                                        Joker(self, (line, column), troops[troop][0], troops[troop][1], troops[troop][2], troops[troop][4])
                    else:
                        try:
                            line = input(f"\n{self.name}: Which line would you place the new one (0-{self.game.nb_lines-1}) ?")
                            i=0
                        except:
                            line = input(f"\n{self.name}: Which line would you place the new one (0-{self.game.nb_lines-1}) ?")
                            i=0
                except:
                    line = input(f"\n{self.name}: Which line would you place the new one (0-{self.game.nb_lines-1}) ?")
                    i=0         
                
            
            

