# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:08:30 2022

@author: Thomas
"""

from character import *
class CustomPieces(Character):#CustomTroop
    def __init__(self, player, position, base_life, base_price, base_strength, custom_pieces):
       super().__init__(player, position, base_life, base_price, base_strength, custom_pieces) 