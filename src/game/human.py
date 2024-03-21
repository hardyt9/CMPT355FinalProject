import player

'''
Class that represents a human player playing apples to apples.
This player should have a name, be able to draw cards, play cards, and pick
a winning card if they are the judge for that round
'''

class Human(player.Player):


    #Inherit from the player class
    def __init__(self, name):
        super().__init__(name)

    #Draw card from the top of the deck
    def draw_card(self, card):
        self.hand.append(card)

    #Play a red card from the player's hand
    def play_card(self):
        print(self.hand)
        picked = input(f"{self.name}, please select a card from your hand: ")
        while picked not in self.hand:
            picked = input(f"{self.name}, invalid card selected, try again: ")

        return picked

    #Pick a winning card if the player is a judge
    def pick_card(self, green, selectable):
        print(selectable)
        picked = input(f"{self.name}, please select a winning card for the green card {green}: ")
        while picked not in selectable:
            picked = input(f"{self.name}, invalid card selected, try again: ")

        return picked
    
    #Switch whether this player is a judge or not
    def switch_judge(self):
        self.judge = not self.judge