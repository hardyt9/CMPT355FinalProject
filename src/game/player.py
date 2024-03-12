from .word_associations import get_adj_associations, get_noun_associations



# create a player class for Apples to Apples which has a name and a hand of red cards and a score checks for AI players and associates correlation
class Player:
    def __init__(self, name,):
        self.name = name             #name of the player
        self.hand = []               #list of red cards in the player's hand
        self.score = 0               #score of the player

    def add_card_to_hand(self, card):
        self.hand.append(card)
    #pick a red card to play for the AI
    def play_red_card(self, green_card):
        
        # get the assoicaitons of the green card to all red cards in the player's hand
        associations = get_adj_associations(green_card, self.hand)
        # loop through the dictionary of associations to get the highest association
                
        for i in associations:
            for j in associations[i]:
                if associations[i][j] == max(associations[i].values()):
                    winner = j
        #return the name of the player who picked the winning red card
        return winner