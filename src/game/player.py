from abc import ABC, abstractmethod

'''
Generic Player Class to act as template for all players.
Implements required methods that all players must implement in order
to play Apples to Apples.
'''

class Player(ABC):

    #Give players a name, empty hand, and intialize them as a regular player
    #Start at 0 points
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.judge = False
        self.points = 0

    @abstractmethod
    def draw_card(self):
        pass

    @abstractmethod
    def play_card(self):
        pass

    @abstractmethod
    def pick_card(self):
        pass

    @abstractmethod
    def switch_judge(self):
        pass