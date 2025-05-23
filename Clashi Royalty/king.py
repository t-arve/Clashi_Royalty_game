# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:11:37 2022

@author: Thomas
"""

from character import *
import random
class King(Character):
    def __init__(self, player, position, base_life, base_price, base_strength, custom_pieces):
       super().__init__(player, position, base_life, base_price, base_strength, custom_pieces) #appelle classe mère
    
    def move(self):
        """
        The function moves the character in the direction it is facing, and if it finds gold, it adds a
        random amount of money to the player's money
        """
    
        position = (self.position[0], self.position[1] + self.direction)
        self.game.place_character(self, position)
        foundgold = random.randint(0,1)
        if(foundgold == 1):
            self.player.money += random.randint(1, 2)