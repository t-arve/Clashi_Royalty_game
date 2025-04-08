# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:08:09 2022

@author: Thomas
"""

from os import system, name

def clear():             
    if (name == 'nt'):                         
        _ = system("cls")

def coloured_name(gametitle):          
    coloured_name = "  ___| |            |    _)  \n |     |  _` |  __| __ \  |  \n |     | (   |\__ \ | | | |  \n\____|_|\__,_|____/_| |_|_|  \n                             \n\n     _ \                    | |         \n    |   |  _ \  |   |  _` | | __| |   | \n    __ <  (   | |   | (   | | |   |   | \n   _| \_\\___/ \__, |\__,_|_|\__|\__, | \n               ____/             ____/ "                  #ya esta
    return coloured_name


gametitle = coloured_name("clashi royal")
gametitle_big = """clashi royalty ;3\n Please, select a gamemode:"""
