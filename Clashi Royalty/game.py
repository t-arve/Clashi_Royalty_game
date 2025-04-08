# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:11:07 2022

@author: Thomas
"""

from console import clear, gametitle_big
from player import *



class Game:
    def __init__(self, player0, player1, nb_lines=6, nb_columns=15):
        """
        PARAM : - player0 : Player
                - player1 : Player
                - nb_lines : float
                - nb_columns : float
        - update players' direction and game
        - initialise player_turn to 0
        """
        self.nb_lines = int(nb_lines)
        self.nb_columns = int(nb_columns)
        self.players = [player0, player1]
        self.player_turn = int(0)
        self.players[0].game = self
        self.players[0].direction = 1

        self.players[1].game = self
        self.players[1].direction = -1

    @property
    def current_player(self):
        return self.players[int(self.player_turn)]

    @property
    def oponent(self):
        if self.player_turn == 0:
            op = 1
        else:
            op = 0
        return self.players[int(op)]

    @property
    def all_characters(self):
        return self.players[0].team + self.players[1].team
    

    def get_character_at(self, position):
        """
        PARAM : - position : tuple
        RETURN : character at the position, None if there is nobody
        """
        check = 0
        for character in self.all_characters:
            if character.position == position:
                char_at = character
                check = True
        if(check):
            return char_at
        else:
            return None


    def place_character(self, character, position):
        """
        place character to position if possible
        PARAM : - character : Character
                - position : tuple
        RETURN : bool to say if placing is done or not
        """
        someoneHere = self.get_character_at(position)
        if someoneHere == None:
            character.position = position
            return True
        if someoneHere != None:
            return False
    

    def draw(self):

        print(gametitle_big,"\n")
        print(
            f"p1 life: {self.players[0].life:<4}            p2 life: {self.players[1].life:>4}")

        print("----"+self.nb_columns*"--"+"----")

        for line in range(self.nb_lines):
            print(f"|{line:>2}|", end="")
            for col in range(self.nb_columns):
                character = self.get_character_at((line, col))
                if character == None:
                    print(".", end=" ")
                else:
                    print(character.design, end=" ")

            print(f"|{line:<2}|")

        print("----"+self.nb_columns*"--"+"----")

        print(
            f"p1 money: {self.players[0].money:<3}    p2 money: {self.players[1].money:>3}")
        troops = Player.get_troops_list(self)
        for troop in troops :
            print(f"{troop[4]} : {troop[3]}({troop[5]})     {troop[0]}HP    {troop[2]}DMG     {troop[1]}$")
        
        
    def play_turn(self):
        """
        play one turn :
            - current player can add a new character
            - current player's character play turn
            - oponent player's character play turn
            - draw the board
        """
        clear()
        self.draw()
        self.current_player.new_character()
        for character in self.current_player.team:
            character.play_turn()
        for character in self.oponent.team:
            character.play_turn()

    def play(self):
        """
        play an entire game : while current player is alive, play a turn and change player turn
        """
        print("PLAY")
        while self.current_player.is_alive and self.oponent.is_alive:
            self.play_turn()
            clear()
            
            if self.player_turn == 0:
                self.player_turn = 1
            else:
                self.player_turn = 0
        clear()
        print(gametitle_big + "\n")
        if(self.current_player.name == "AI"):
            print("pc wins")
            self.leaderboard()
            input("\nPress enter to go back to the menu")
            return
