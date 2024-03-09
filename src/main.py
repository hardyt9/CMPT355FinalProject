from game import ApplesToApples

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
