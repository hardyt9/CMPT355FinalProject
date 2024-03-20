from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.judge = False

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