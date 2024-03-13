import random
from .player import Player
from .deck import Deck
from .word_associations import get_adj_associations, get_noun_associations


'''
TODO Documentation
#create a game class for Apples to Apples with the list of players
'''
class ApplesToApples():
    '''
    TODO Documentation
    #initialize the game with four to ten players from inputed list of players and the red and green decks
    '''
    def __init__(self, players, red_deck, green_deck):
        #initialize the list of players and the red and green decks
        self.players = [Player(name) for name in players] #create a list of player instances with name and empty hand
        self.red_deck = red_deck                          #list of red cards
        self.green_deck = green_deck                      #list of green cards

        # shuffle decks
        self.red_deck.shuffle() #shuffle the red deck
        self.green_deck.shuffle() #shuffle the green deck
        
        # who ever is the first judge will be randomly chosen
        self.current_judge_index = random.randint(0, len(self.players)-1) #randomly choose the first judge
        # deal hands to players
        self.deal_hands()
    
    '''
    TODO Documentation
    # randomly pick 7 red cards from red deck to give to each player in the game
    '''
    def deal_hands(self):
        for player in self.players: #for each player in the game
            # Randomly create the player's hand by drawing 7 cards from the red deck
            for _ in range(7):
                card = self.red_deck.draw_card() #remove the card from the red deck
                player.hand.append(card) #add the card to the player's hand

    '''
    TODO Documentation
    # Executes the game while it is not over calls pick and play a round
    '''
    def start_game(self):
        while not self.game_over():
            self.pick_and_play_round()

    '''
    TODO Documentation
    #print the current judge's name
    #pick the top green card from the shuffled deck
    #print the green card picked by the judge
    #print the red cards picked by other players
    #for each player and their red card
    #print the player's name and their red card
    #print the winner's name
    #for each player in the game
    #if the player's name is the winner's name
    #add 1 to the player's score
    #print the player's name and their score
    #if the player's score is 4
    #print the player's name and that they have won the game
    #end the game
    '''
    def pick_and_play_round(self):
        #current judge is the player at the current judge index
        current_judge = self.players[self.current_judge_index]                         
        print(f"\nJudge: {current_judge.name}")  
                                      
        green_card = self.green_deck.draw_card()  
        print(f"Green card drawn: {green_card}") 

        #Players pick one red card each                                     
        red_cards = self.pick_red_cards(green_card)            
        print("Red cards picked by other players:")                  
        for name, card in red_cards.items():                                            
            print(f"{name}: {card}")  

        #the judge picks the winning red card                                                 
        winner_name = self.pick_winner(red_cards,green_card)                             
        print(f"Winner: {winner_name}")   
                                              
        for player in self.players:                                                    
            if player.name == winner_name:                                              
                player.score += 1                                         
                print(f"{player.name} won the round and has {player.score} point(s).") 
                if player.score == 4:                                                  
                    print(f"{player.name} has won the game!")                          
                    return     

        #change the judge to the next player in the list (moves to the next player in the list)                                                     
        self.current_judge_index = (self.current_judge_index + 1) % len(self.players)   
    
    '''
    TODO Documentation
    # Players pick one red card each
    '''
    def pick_red_cards(self, green_card):    
        #create a dictionary for the red cards picked by the players
        red_cards = {}                                         
        #for each player in the game
        for i, player in enumerate(self.players): 
            #if the player is not the judge                                                  
            if i != self.current_judge_index:
                #if the player is an AI                                                   
                if player.name == "AI": 
                    #get the assoicaitons of the green card to all red cards in the player's hand using API                                                            
                    card = player.play_red_card(green_card)
                    #append name and card to dictionary of red cards picked by the players and by the AI
                    red_cards[player.name] = card

                #if player is human                                       
                else:  
                    #prompt the player to pick a red card from their hand                                                                            
                    print(f"\n{player.name}, it's your turn.")  
                    print("")
                    #print the player's hand                                    
                    print("Your hand:", player.hand) 
                    #prompt the player to enter the index of the red card they want to play                                              
                    card_index = int(input("Enter the index of the red card you want to play: ")) 
                    print("")
                    #remove the card from the player's hand and add a new card from the red deck to the player's hand  
                    card = player.hand.pop(card_index)                                           
                    player.hand.append(self.red_deck.draw_card())
                    #add the player's name and the card they picked to the dictionary of red cards picked by the players and by the AI
                    red_cards[player.name] = card 
        #return the dictionary of red cards picked by the players and by the AI                                                                                                       
        return red_cards                                                                            

    '''
    TODO Documentation
    # the judge picks the winning red card by examining the red cards picked by the players and choosing the highest association
    '''
    def pick_winner(self, red_cards, green_card):
        #use get adj associations to get the association of the green card to the red card chosen by the players for the round
        associations = get_adj_associations(green_card, red_cards)
        #loop through the assoication dictionary and find the red card with the highest association to the green card (value)
        # format of dictionary is {adjective: {noun: similarity}}
        for i in associations:
            for j in associations[i]:
                if associations[i][j] == max(associations[i].values()):
                    winner = j
        #return the name of the player who picked the winning red card
        return winner

    '''
    TODO Documentation 
    # create a method to check if the game is over
    '''
    def game_over(self):
        # check to see if any player has 4 points
        return any(player.score == 4 for player in self.players)