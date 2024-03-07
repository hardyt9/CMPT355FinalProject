import random
from difflib import SequenceMatcher

# create a player class for Apples to Apples which has a name and a hand of red cards and a score checks for AI players and associates correlation
class Player:
    def __init__(self, name, is_ai=False):
        self.name = name        #name of the player
        self.hand = []          #list of red cards in the player's hand
        self.score = 0          #score of the player
        self.is_ai = is_ai      #check if the player is an AI
        self.correlation = {}   #correlation of the player's hand to the green card

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def associate_correlation(self, green_card, red_cards):
        if self.is_ai:
            if green_card not in self.correlation:
                self.correlation[green_card] = {'Perfect Match': [], 'High Match': [], 'Low Match': []}
            for card in red_cards:
                similarity = self.calculate_similarity(card, green_card)
                if similarity == 1:
                    self.correlation[green_card]['Perfect Match'].append(card)
                elif similarity >= 0.7:
                    self.correlation[green_card]['High Match'].append(card)
                elif similarity >= 0.5:
                    self.correlation[green_card]['Low Match'].append(card)

    def play_red_card(self, green_card):
        if self.is_ai:
            best_match = None
            best_similarity = 0
            for card in self.hand:
                similarity = self.calculate_similarity(card, green_card)
                if similarity > best_similarity:
                    best_similarity = similarity
                    best_match = card
            return best_match

    def calculate_similarity(self, card1, card2):
        return SequenceMatcher(None, card1, card2).ratio()

#------------------------------------------------------------------------------------------------      
#create a game class for Apples to Apples with the list of players
class ApplesToApples():
    #initialize the game with four to ten players from inputed list of players and the red and green decks
    def __init__(self, players, red_deck, green_deck):
        #initialize the list of players and the red and green decks
        self.players = [Player(name) for name in players] #create a list of player instances with name and empty hand
        self.red_deck = red_deck                          #list of red cards
        self.green_deck = green_deck                      #list of green cards

        # shuffle decks
        random.shuffle(self.red_deck) #shuffle the red deck
        random.shuffle(self.green_deck) #shuffle the green deck
        
        # who ever is the first judge will be randomly chosen
        self.current_judge_index = random.randint(0, len(self.players)-1) #randomly choose the first judge
        # deal hands to players
        self.deal_hands()
    
    # randomly pick 7 red cards from red deck to give to each player in the game
    def deal_hands(self):
        for player in self.players: #for each player in the game
            # Randomly create the player's hand by drawing 7 cards from the red deck
            for i in range(7):
                card = self.red_deck.pop(0) #remove the card from the red deck
                player.hand.append(card) #add the card to the player's hand

    # Executes the game while it is not over calls pick and play a round
    def start_game(self):
        while not self.game_over():
            self.pick_and_play_round()

    def pick_and_play_round(self):
        current_judge = self.players[self.current_judge_index]                          #current judge is the player at the current judge index
        print(f"\nJudge: {current_judge.name}")                                         #print the current judge's name
        green_card = self.pick_green_card()                                             #pick the top green card from the shuffled deck
        print(f"Green card picked: {green_card}")                                       #print the green card picked  
        red_cards = self.pick_red_cards()                                               #Players pick one red card each
        print("Red cards picked by other players (in random order):")                   #print the red cards picked by other players
        for name, card in red_cards.items():                                            #for each player and their red card
            print(f"{name}: {card}")                                                    #print the player's name and their red card
        winner_name = self.pick_winner(red_cards)                                       #the judge picks the winning red card
        print(f"Winner: {winner_name}")                                                 #print the winner's name
        for player in self.players:                                                     #for each player in the game
            if player.name == winner_name:                                              #if the player's name is the winner's name
                player.score += 1                                                       #add 1 to the player's score
                print(f"{player.name} won the round and has {player.score} points.")    #print the player's name and their score
                if player.score == 4:                                                   #if the player's score is 4
                    print(f"{player.name} has won the game!")                           #print the player's name and that they have won the game
                    return                                                              #end the game
        self.current_judge_index = (self.current_judge_index + 1) % len(self.players)   #change the judge to the next player in the list (moves to the next player in the list)

    # pick the top green card from the shuffled deck
    def pick_green_card(self):
        return self.green_deck.pop(0)
    
    # Players pick one red card each
    def pick_red_cards(self):                                                                       #Players pick one red card each
        red_cards = {}                                                                              #create a dictionary for the red cards                        
        green_card = self.green_deck[0]                                                             # Get the current round's green card   
        print(f"\nGreen card for this round: {green_card}")                                         #print the green card for this round
    
        for i, player in enumerate(self.players):                                                   #for each player in the game
            if i != self.current_judge_index:                                                       #if the player is not the judge
                if player.name == "AI":                                                             #if the player is an AI
                    card = player.play_red_card(green_card)                                         #play the best red card
                else:                                                                               # if the player is not an AI
                    print(f"\n{player.name}, it's your turn.")                                      #prompt the player to pick a red card
                    print("Your hand:", player.hand)                                                #print the player's hand
                    card_index = int(input("Enter the index of the red card you want to play: "))   #prompt the player to enter the index of the red card they want to play
                    card = player.hand.pop(card_index)                                              #remove the card from the player's hand
                red_cards[player.name] = card                                                       #add the player's name and their red card to the dictionary
                for p in self.players:                                                              #for each player in the game
                    if p != player:                                                                 #if the player is not the current player
                        p.associate_correlation(green_card, [card])                                 #associate the correlation of the player's hand to the green card
        return red_cards                                                                            #return the dictionary of red cards

    
   
    
    # the judge picks the winning red card
    def pick_winner(self, red_cards):
        return random.choice(list(red_cards.keys()))

    # create a method to check if the game is over
    def game_over(self):
        # check to see if any player has 4 points
        return any(player.score == 4 for player in self.players)

    
#------------------------------------------------------------------------------------------------
# set up the game, create data for the green deck and the red deck 
# generate a list of adjectives and a list of nouns for game play from imported text files
def main():
    # from the text files, create the red and green decks
    filename1 = "red_deck.txt"
    filename2 = "green_deck.txt"
    red_deck = []
    green_deck = []
    with open(filename1, 'r') as file:
        for line in file:
            red_deck.append(line.strip())

    with open(filename2, 'r') as file:
        for line in file:
            green_deck.append(line.strip())
    
    # create a list of players
    players = ["Tyler", "Darion", "Aiden", "Malcom", "AI"]
    # create an instance of the game
    game = ApplesToApples(players, red_deck, green_deck)
    # start the game
    game.start_game()
#------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
