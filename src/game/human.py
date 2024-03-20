import player

class Human(player.Player):

    def __init__(self, name):
        super().__init__(name)

    def draw_card(self, deck):
        self.hand.append(deck.pop())

    def play_card(self):
        print(self.hand)
        picked = input(f"{self.name}, please select a card from your hand: ")
        while picked not in self.hand:
            picked = input(f"{self.name}, invalid card selected, try again: ")

        return picked

    def pick_card(self, green, selectable):
        print(selectable)
        picked = input(f"{self.name}, please select a winning card for the green card {green}: ")
        while picked not in selectable:
            picked = input(f"{self.name}, invalid card selected, try again: ")

        return picked
    
    def switch_judge(self):
        self.judge = not self.judge