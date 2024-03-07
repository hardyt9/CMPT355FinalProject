import random

# create a player class for Apples to Apples which has a name and a hand
class Player: 
    # initialize the player with the name and empty hand
    def __init__(self, name):
        self.name = name 
        self.hand = [] 
        self.score = 0

#------------------------------------------------------------------------------------------------      
#create a game class for Apples to Apples with the list of players
class ApplesToApples():
    #initialize the game with four to ten players from inputed list of players and the red and green decks
    def __init__(self, players, red_deck, green_deck):
        #initialize the list of players and the red and green decks
        self.players = self.create_players(players)
        self.red_deck = red_deck
        self.green_deck = green_deck

        # shuffle the red and green decks
        random.shuffle(self.red_deck)
        random.shuffle(self.green_deck)
        
        # who ever is the first judge will be randomly chosen
        self.judge = self.choose_first_judge()
        # deal hands to players
        self.deal_hands()
        # start the game
        self.start_game()

    # method to create instance of players from list of players
    def create_players(self, player_names):
        #create a list of player instances
        players = []
        for name in player_names:
            players.append(Player(name)) #create a list of player instances with name and empty hand
        return players
    
    # randomly choose who will go first as the judge
    def choose_first_judge(self):
        return random.choice(self.players)

    # randomly pick 7 red cards from red deck to give to each player in the game
    def deal_hands(self):
        for player in self.players:
            # Rnadomly create the player's hand by drawing 7 cards from the red deck
            for i in range(7):
                card = self.red_deck.pop(0)
                player.hand.append(card)

    # start the game
    def start_game(self):
        while not self.game_over():
            print(f"\nJudge: {self.judge.name}")
            # pick a green card from the deck
            green_card = self.pick_green_card()
            print(f"Green card picked: {green_card}")
            # other players pick red cards
            red_cards = self.pick_red_cards(self.players)
            print("Red cards picked by other players (in random order):")
            for name, card in red_cards.items():
                print(f"{name}: {card}")
            # judge picks the winning red card
            winner_name = self.pick_winner(red_cards)
            print(f"Winner: {winner_name}")
            # update winning player score 
            for player in self.players:
                if player.name == winner_name:
                    player.score += 1
                    print(f"{player.name} won the round and has {player.score} points.")
                    if player.score == 4:
                        print(f"{player.name} has won the game!")
                        return
        # choose next judge
        self.judge = self.choose_next_judge()



    # pick the top green card from the shuffled deck
    def pick_green_card(self):
        return self.green_deck.pop(0)
    
    # Players pick one red card each
    def pick_red_cards(self, players):
        # store the red card that each player picks in dictionary
        red_cards = {}
        for player in players:
            # if the player is not the judge, they will pick a red card from their hand
            if player != self.judge:
                card = random.choice(player.hand)
                # remove the red card from the player's hand
                player.hand.remove(card)
                # store the red card in the dictionary with the player's name as the key
                red_cards[player.name] = card
        return red_cards
    
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
filename1 = "red_deck.txt"
filename2 = "green_deck.txt"
# red deck is a list of nouns
red_deck = []
# green deck is a list of adjectives
green_deck = []

# create a list of nouns to append to the red deck (from filename1)
with open(filename1, 'r') as file:
    for line in file:
        red_deck.append(line.strip())

# create a list of adjectives to append to the green deck (from filename2))
with open(filename2, 'r') as file:
    for line in file:
        green_deck.append(line.strip())
    
# create list of player from 4 to 10 players (can start with up to four players and add more as needed)
players = ["Tyler", "Darion", "Aiden", "Malcom","AI"] 

# create a game instance with the list of players and the red and green decks
game = ApplesToApples(players, red_deck, green_deck)
