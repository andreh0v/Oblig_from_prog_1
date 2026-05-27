#Dette skal være et blackjack ligende
import random

class card:
    def __init__(self, rank, value):
        self.rank = rank
        self.value = value
    def __str__(self):
        return f"Rank: {self.rank}, Value: {self.value}"

#The cards used
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

class Deck:
    def __init__(self):
        self.cards = []
        for rank, value in zip(ranks, values):
            for i in range(4):
                self.cards.append(card(rank, value))
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        return self.cards.pop()

#Hand value function
def calculate_hand(hand):
    total = sum(card.value for card in hand)
    aces = sum(1 for card in hand if card.rank == "A")
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

#Player function
class Player:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.hand = []
        self.chips = 100
        self.bet = 0
    def add_card(self, card):
        self.hand.append(card)
    def hand_value(self):
        return calculate_hand(self.hand)

#Dealer code
class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.hand = []
    def add_card(self, card):
        self.hand.append(card)
    def hand_value(self):
        return calculate_hand(self.hand)

#Placing bets function
def place_bet(player):
    while True:
        bet = int(input("Place your bet: "))
        if 0 < bet <= player.chips:
            player.bet = bet
            break
        else:
            print("Invalid bet!")

#Dealing cards function
def deal_starting_cards(player, dealer, deck):
    for i in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())

#Checking for blackjack
def check_blackjack(player, dealer):
    if player.hand_value() == 21:
        print("Blackjack! You win!")
        player.chips += player.bet * 2
        return True
    elif dealer.hand_value() == 21:
        print("Dealer has Blackjack! You lose!")
        player.chips -= player.bet
        return True
    return False

#Player turn
def player_turn(player, deck):
    while True:
        print(f"Your hand value: {player.hand_value()}")
        choice = input("Hit or Stand? ").lower()
        if choice == "hit":
            player.add_card(deck.deal())
        elif choice == "stand":
            break
        if player.hand_value() > 21:
            print("Bust! You lose your bet!")
            player.chips -= player.bet
            return False
    return True

#Dealer pulling cards until 17
def dealer_turn(dealer, deck):
    while dealer.hand_value() <= 16:
        dealer.add_card(deck.deal())
        print(f"Dealer draws: {dealer.hand[-1]}")
    print(f"Dealer's final hand value: {dealer.hand_value()}")
    if dealer.hand_value() > 21:
        print("Dealer busts! You win!")
        return False
    return True

#Comparing hands
def compare_hands(player, dealer):
    player_score = player.hand_value()
    dealer_score = dealer.hand_value()
    if player_score > dealer_score:
        print("You win!")
        player.chips += player.bet
    elif dealer_score > player_score:
        print("Dealer wins!")
        player.chips -= player.bet
    else:
        print("Draw!")

#Main game function
#Main game function
def play_blackjack():
    deck = Deck()
    deck.shuffle()
    player = Player()
    dealer = Dealer()
    print(f"Hey {player.name}, ready to play Blackjack!?")

    while player.chips > 0:
        player.hand = []
        dealer.hand = []
        place_bet(player)
        deal_starting_cards(player, dealer, deck)
        print(f"Your hand: {[str(c) for c in player.hand]}")
        print(f"Dealer shows: {dealer.hand[0]}")
        if not check_blackjack(player, dealer):
            if player_turn(player, deck):
                if dealer_turn(dealer, deck):
                    compare_hands(player, dealer)
        print(f"You have {player.chips} chips remaining!")

        if player.chips > 0:
            again = input("Play again? (yes/no): ").lower()
            if again != "yes":
                break

    print("Game over!")

play_blackjack()