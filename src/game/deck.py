import random

'''
TODO Documentation
'''
class Deck():
    '''
    TODO Documentation
    '''
    def __init__(self, filename):
        self.cards = []
        self.size = 0
        self.filename = filename

        with open(filename, 'r') as file:
            for line in file:
                self.cards.append(line.strip())
                self.size += 1

    '''
    TODO Documentation
    '''
    def shuffle(self):
        random.shuffle(self.cards)

    '''
    TODO Documentation
    '''
    def draw_card(self):
        self.size -= 1
        return self.cards.pop(0)
