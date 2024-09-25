import random
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self, num_players):
        hand_size = len(self.cards) // num_players
        hands = [self.cards[i * hand_size:(i + 1) * hand_size] for i in range(num_players)]
        return hands


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        if self.hand:
            return self.hand.pop(0)
        return None

    def has_cards(self):
        return len(self.hand) > 0

    def __repr__(self):
        return self.name


def play_duck_game(num_players=4):
    print("\n*** لعبة البطة تبدأ الآن! ***\n")

    deck = Deck()
    hands = deck.deal(num_players)
    players = [Player(f"Player {i + 1}", hand) for i, hand in enumerate(hands)]

    for player in players:
        print(f"{player}'s hand: {player.hand}\n")

    round_number = 1
    while True:
        print(f"\n--- الجولة {round_number} ---")

        active_players = [player for player in players if player.has_cards()]

   
        if len(active_players) == 1:
            print(f"\n{active_players[0]} هو البطة!")
            break

        for player in active_players:
            if len(player.hand) >= 2 and player.hand[0].rank == player.hand[1].rank:
                card1 = player.play_card()
                card2 = player.play_card()
                print(f"{player} يلعب ورقتين: {card1} و {card2}")
            else:
                card = player.play_card()
                print(f"{player} يلعب: {card}")

            if not player.has_cards():
                print(f"{player} قد فاز!")
                players.remove(player)

        if all(not player.has_cards() for player in players):
            print("انتهت اللعبة، جميع اللاعبين نفدت أوراقهم!")
            break

        for player in active_players:
            print(f"{player} لديه {len(player.hand)} ورقة متبقية")

        round_number += 1



num_players = int(input("أدخل عدد اللاعبين (2-4): "))
while num_players < 2 or num_players > 4:
    num_players = int(input("الرجاء إدخال عدد صحيح بين 2 و 4: "))

play_duck_game(num_players)
