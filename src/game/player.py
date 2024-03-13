from .word_associations import get_adj_associations, get_noun_associations


'''
TODO Documentation
# create a player class for Apples to Apples which has a name and a hand of red cards and a score checks for AI players and associates correlation
'''
class Player:
    '''
    TODO Documentation
    '''
    def __init__(self, name,):
        self.name = name             #name of the player
        self.hand = []               #list of red cards in the player's hand
        self.score = 0               #score of the player
    
    '''
    TODO Documentation
    '''
    def add_card_to_hand(self, card):
        self.hand.append(card)

    '''
    TODO Documentation
    '''
    def play_red_card(self, green_card):
        all_associations = get_adj_associations(green_card, self.hand)

        # loop through the dictionary of associations to get the highest association
        max_association_value = 0
        for adjective, associations in all_associations.items():
            for noun, association_value in associations.items():
                if association_value > max_association_value:
                    red_card_play = noun
                    max_association_value = association_value
        return red_card_play