import random


class Card:
    def __init__(self, rank, value):
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"Rank: {self.rank}, Value: {self.value}"


# The cards used
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


class Deck:
    def __init__(self):
        self.cards = []
        for rank, value in zip(ranks, values):
            for i in range(4):
                self.cards.append(Card(rank, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


# Hand value function
def calculate_hand(hand):
    total = sum(card.value for card in hand)
    aces = sum(1 for card in hand if card.rank == "A")
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


# Player class
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


# Dealer class
class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def hand_value(self):
        return calculate_hand(self.hand)


# Placing bets function
def place_bet(player):
    while True:
        try:
            bet = int(input(f"You have {player.chips} chips. Place your bet: "))
            if 0 < bet <= player.chips:
                player.bet = bet
                player.chips -= bet  # Chips are taken placed on the table immediately
                break
            else:
                print("Invalid bet!")
        except ValueError:
            print("Please enter a valid number.")


# Dealing cards function
def deal_starting_cards(player, dealer, deck):
    for i in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())


# Checking for initial blackjack
def check_blackjack(player):
    if player.hand_value() == 21:
        return True
    return False


# Player turn
def player_turn(player, deck):
    while True:
        print(f"Your hand value: {player.hand_value()}")
        if player.hand_value() > 21:
            print("Bust! You went over 21!")
            return False

        choice = input("Hit or Stand? ").lower()
        if choice == "hit":
            player.add_card(deck.deal())
            print(f"You drew: {player.hand[-1]}")
        elif choice == "stand":
            break
    return True


# Dealer turn
def dealer_turn(dealer, deck):
    # Standard casino rules: Dealer hits until reaching 17 or higher
    while dealer.hand_value() < 17:
        dealer.add_card(deck.deal())
        print(f"Dealer draws: {dealer.hand[-1]}")
    print(f"Dealer's final hand value: {dealer.hand_value()}")

    if dealer.hand_value() > 21:
        print("Dealer busts!")
        return False
    return True


# Centralized bet settlement
def settle_bet(player, outcome):
    if outcome == "blackjack":
        # Blackjack pays 2:1 based on your prompt (Returns bet + 2x bet profit)
        winnings = player.bet * 3
        player.chips += winnings
        print(f"Blackjack! You win {winnings} chips!")
    elif outcome == "win":
        # Normal win pays 1:1 (Returns bet + 1x bet profit)
        winnings = player.bet * 2
        player.chips += winnings
        print(f"You win! You receive {winnings} chips.")
    elif outcome == "draw":
        # Push (Returns your original bet)
        player.chips += player.bet
        print("Draw! Your bet has been returned.")
    elif outcome == "lose":
        # Chips were already deducted, so we just print the message
        print("Dealer wins! You lose your bet.")


# Main game function
def play_blackjack():
    player = Player()
    dealer = Dealer()
    print(f"Hey {player.name}, ready to play Blackjack!?\n")

    while player.chips > 0:
        # Fresh deck every round to prevent running out of cards
        deck = Deck()
        deck.shuffle()

        player.hand = []
        dealer.hand = []

        place_bet(player)
        deal_starting_cards(player, dealer, deck)

        print(f"\nYour hand: {[str(c) for c in player.hand]} (Value: {player.hand_value()})")
        print(f"Dealer shows: {dealer.hand[0]}")

        outcome = ""

        # 1. Check for instant Blackjack
        if check_blackjack(player):
            outcome = "blackjack"
        else:
            # 2. Player's turn
            player_alive = player_turn(player, deck)

            if not player_alive:
                outcome = "lose"
            else:
                # 3. Dealer's turn
                print("\n--- Dealer's Turn ---")
                print(f"Dealer's hidden card was: {dealer.hand[1]}")
                dealer_alive = dealer_turn(dealer, deck)

                if not dealer_alive:
                    outcome = "win"
                else:
                    # 4. Compare hands if nobody busted
                    player_score = player.hand_value()
                    dealer_score = dealer.hand_value()

                    if player_score > dealer_score:
                        outcome = "win"
                    elif dealer_score > player_score:
                        outcome = "lose"
                    else:
                        outcome = "draw"

        # 5. Financial settlement happens here
        settle_bet(player, outcome)
        print(f"You now have {player.chips} chips.\n")

        if player.chips > 0:
            again = input("Play again? (yes/no): ").lower()
            if again != "yes":
                break

    print("Game over!")


play_blackjack()