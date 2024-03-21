import player
import judge

'''
Class that represents the agent playing apples to apples. Should be able to 
draw cards, play red cards when a regular player, and judge red cards when a
judge. Requires a judge function in order to judge cards. By default, it picks
the red card most similar to the green card for that round.
'''

class AI(player.Player):

    #inherit from Player class
    def __init__(self, name, judge_style=None):
        super().__init__(name)

        #Store card correlations
        self.correlations = {}
        
        #red cards that have been played up until now
        self.played = {}

        #Grab judge function
        if judge_style is None:
            self.judge_style = judge.default_judge
        else:
            self.judge_style = judge_style
        

    #Grab a card and add to hand
    def draw_card(self, card):
        self.hand.append(card)

    #play red card
    def play_card(self, green_card):
        pass

    #judge cards
    def pick_card(self, green_card, selectable):
        pass

    #Switch whether agent is a judge or not
    def switch_judge(self):
        self.judge = not self.judge