from abc import ABC, abstractmethod

class Player(ABC):

    @abstractmethod
    def draw_card(self):
        pass

    @abstractmethod
    def play_card(self):
        pass

    @abstractmethod
    def pick_card(self):
        pass
