from cards import Card, Deck, Player

class Game:
    def __init__(self, p1:Player, p2:Player, p1_score:int, p2_score:int):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = p1_score
        self.p2_score = p2_score

    def play_game(self):
        deck1 = self.p1.draw()
        deck2 = self.p2.draw()
        deck1_score = self.p1_score
        deck2_score = self.p2_score
        if deck1 or deck2 == None:
            return deck1_score, deck2_score
        print(f"Player 1 deck: {deck1}; Player 2 deck: {deck2}")
        if deck1 == None or deck2 == None:
            return
        self.fight(deck1, deck2)



    def fight(self, card1:Card, card2:Card):
        res_1 = card1.attack - card2.defense
        res_2 = card2.attack - card1.defense

        if res_1 > res_2:
            self.p1_score += 1
            self.play_game()

        elif res_1 < res_2:
            self.p2_score += 1
            self.play_game()

        elif res_1 == res_2:
            self.play_game()





# Створення карт
card1 = Card("Дракон", 10, 6)
card2 = Card("Лицар", 7, 5)
card3 = Card("Маг", 8, 3)
card4 = Card("Орк", 6, 7)
card5 = Card("Ельф", 5, 4)
card6 = Card("Гном", 6, 6)

# Створення колод
deck1 = Deck()
deck1.add_card(card1)
deck1.add_card(card3)
deck1.add_card(card5)

deck2 = Deck()
deck2.add_card(card2)
deck2.add_card(card4)
deck2.add_card(card6)

# Створення гравців
player1 = Player("Олексій", deck1)
player2 = Player("Марія", deck2)

# Запуск гри
game = Game(player1, player2, 0, 0)
final_scores = game.play_game()
print(f"\nФінальний рахунок: {final_scores}")