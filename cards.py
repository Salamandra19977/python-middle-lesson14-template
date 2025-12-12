class Card:
    def __init__(self, name:str, attack:int, defense:int):
        self.name = name
        self.attack = attack
        self.defense = defense
    def __str__(self):
        return f"Name: {self.name}, Attack: {self.attack}, Defence: {self.defense} "


class Deck:
    cards = []
    def __init__(self):
        pass


    def add_card(self, card):
        self.cards.append(card)
        return self.cards

    def draw_card(self):
        if self.cards:
            print(self.cards[len(self.cards) -1])
            self.cards.pop(len(self.cards) - 1)
        else:
            print("Deck is Empty")
            return 0


class Player:
    def __init__(self, name:str, deck:Deck):
        self.name = name
        self.deck = deck

    def draw(self):
        Deck.draw_card(self.deck)


deck1 = Deck()
deck1.add_card(Card("Воїн", 5, 5))
player1 = Player("Олексій", deck1)
card = player1.draw()




