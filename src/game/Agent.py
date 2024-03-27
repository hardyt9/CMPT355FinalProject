JUDGE_STYLES = ["Default", "Contrarian", "Funny", "Dark"]
MAX_CARDS = 3
import word_associations as wrd
import sys

'''
Class that represents the agent playing apples to apples. Should be able to 
draw cards, play red cards when a regular player, and judge red cards when a
judge. Requires a judge function in order to judge cards. By default, it picks
the red card most similar to the green card for that round.
'''

class Agent:

    def __init__(self, red, green):
        self.hand = []
        self.played = []
        self.points = 0
        self.red_filename = red
        self.green_filename = green
        self.removed = {'R':[], 'G':[]}

    def add_card(self):

        while len(self.hand) < MAX_CARDS:

            card_name = input("Please enter a card: ")
            self.hand.append(Card(card_name, 'R'))


    def play_card(self, green_card):
        best = -100

        for i in self.hand:
            if i.correlations[green_card][i.name] > best:
                best = i.correlations[green_card][i.name]
                chosen = i

        self.hand.remove(chosen)
        return chosen.name
    
    def remove_from_pool(self, reds, green):

        for i in reds:

            self.removed['R'].append(i)

        self.removed['G'].append(green)

class Card:

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.played = False
        if self.type == 'R':
            self.correlations = wrd.get_noun_associations(self.name)
        else:
            self.correlations = wrd.get_adj_associations(self.name)

    def played(self):
        self.played = True

    def get_Correlations(self, correlations):
        
            self

        # for i in JUDGE_STYLES:
        #     match i:
        #         case "Default":
        #             self.correlations[i] = words

        #         case "Contrarian":
        #             opp = words
        #             self.correlations[i] =

if __name__ == '__main__':

    if len(sys.argv) < 5:
        print("USAGE: ./agent #Players #Points GreenExt RedExt")
        exit()

    agent = Agent("red_deck.txt", "green_deck.txt")

    agent.add_card()

    player_pts = [0 for i in range(int(sys.argv[1]))]

    WINPOINT = int(sys.argv[2])

    while WINPOINT not in player_pts:

        role = input("0 - Player; else - Judge: ")

        if not int(role):

            green = input("Green card: ")

            red = agent.play_card(green)
            print(f"I play {red}")

            winner = input("Which player won? ")
            player_pts[int(winner) - 1] += 1

        else:
            green = input("Green card: ")
            round = []

            for i in range(len(player_pts)):
                round.append(input(f"Enter player's card: "))

            print(f"Picked: {round[0]}")
            winner = input("Which player won? ")
            player_pts[int(winner) - 1] += 1


    print(f"\nGAMEOVER - Player {player_pts.index(WINPOINT) + 1} wins!\n")
