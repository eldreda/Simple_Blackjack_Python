import random

symbol = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
rank = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
        'Jack', 'Queen', 'King', 'Ace']
value = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
         'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
chips = 100
player_going = 1


# Make class for Cards
class Card():
    def __init__(self, init_symbol, init_rank):
        self.symbol = init_symbol
        self.rank = init_rank

    # To print the card out
    def __str__(self):
        return f"{self.rank} of {self.symbol}"


# Make class for Decks
class Deck():
    def __init__(self):
        self.list = []
        for i in symbol:
            for j in rank:
                card = Card(i, j)
                self.list.append(card)

    def shuffle(self):
        random.shuffle(self.list)


# Make class for the cards in the hand of player / dealer
class Hand():
    def __init__(self, role):
        self.role = role
        self.cards = []
        self.score = 0
        self.ace = 0
        self.hide = 1

    # Add one new card from the deck
    def hit(self):
        card = deck.list.pop()
        self.cards.append(card)
        self.score += value[card.rank]
        if card.rank == 'Ace':
            self.ace += 1

    def adjust_for_ace(self):
        while self.score > 21 and self.ace:
            self.score -= 10
            self.ace -= 1


# Helper function
def ask_bet():
    while True:
        try:
            bet_amount = int(input("How many chips would you like to bet?"))

        except:
            print("You must input an integer!")

        else:
            if bet_amount > chips:
                print("Please place a bet less than or equal to the chips that you have!")
                continue
            print(f"You have successfully placed a bet of {bet_amount} chips!")
            return bet_amount


# Helper function
def check_win():
    if player.score > 21:
        chosen_winner = "DEALER"
    elif dealer.score > 21:
        chosen_winner = "PLAYER"
    elif player.score == dealer.score:
        chosen_winner = "BOTH"
    elif player.score < dealer.score:
        chosen_winner = "DEALER"
    elif player.score > dealer.score or player.score == 21:
        chosen_winner = "PLAYER"

    return chosen_winner


# Helper function
def print_hand(role):
    counter = 1
    print()
    print(f"{role.role}'s Hand: \n")
    for card in role.cards:
        if counter == 1 and role.role == 'Dealer' and role.hide == 1:
            print(" <Hidden Card>")
            counter += 1
            continue

        counter += 1
        print(f" {card}")


# Helper function
def dealer_plays():
    dealer.hide = 0
    print_hand(dealer)
    print_hand(player)
    while dealer.score < 17:
        print("The dealer is playing!")
        dealer.hit()
        dealer.adjust_for_ace()
        print_hand(dealer)
        print_hand(player)


# Helper function
def player_choices():
    while True:

        try:
            chosen_choice = input("\nWould you like to Hit or Stand? Enter 'h' or 's' \n")
            chosen_choice = chosen_choice.lower()

        except:
            print("Please enter either 'h' or 's'")

        else:
            if chosen_choice == 'h':
                return 1

            elif chosen_choice == 's':
                dealer_plays()
                return 0


# Helper function
def play_again():
    while True:
        try:
            input_answer = input("Would you like to play another game? Enter 'y' or 'n'")
            input_answer = input_answer.lower()
            if input_answer == 'y' or input_answer == 'n':
                return input_answer
            else:
                print("Please enter either 'y' or 'n'! ")
                continue

        except:
            print("Please enter either 'y' or 'n'! ")


def reset():
    global chips
    init_deck = Deck()
    init_dealer = Hand("Dealer")
    init_player = Hand("Player")
    return init_deck, init_dealer, init_player


while True:
    deck, dealer, player = reset()
    deck.shuffle()
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.')
    print(f"You have {chips} chips!")

    bet = ask_bet()

    for i in range(2):
        player.hit()
        player.adjust_for_ace()
        dealer.hit()
        dealer.adjust_for_ace()

    print_hand(dealer)
    print_hand(player)

    if player.score <= 21:
        player_going = player_choices()

        while player_going:
            player.hit()
            player.adjust_for_ace()
            print_hand(dealer)
            print_hand(player)
            if player.score > 21:
                player_going = 0
                dealer.hide = 0
                break
            player_going = player_choices()
            print(deck)
    elif player.score == 21:
        player.going = 0
        dealer.hide = 1
        dealer_plays()

    winner = check_win()
    print("Final Standings: \n \n")
    print_hand(dealer)
    print(f"Dealer's score: {dealer.score}")
    print_hand(player)
    print(f"Player's score: {player.score}")
    print(f"{winner} WINS!")

    if winner == 'PLAYER':
        chips += bet
        print(f"Player's winnings stand at: {chips} chips")
    elif winner == 'DEALER':
        chips -= bet
        print("Player has lost the chips")
        print(f"Player's now have: {chips} chips")
    elif winner == 'BOTH':
        print("Dealer's score is equal to the player's score. It's a push!")
        print(f"Player's now have: {chips} chips")

    answer = play_again()
    if answer == 'y':
        if chips <= 0:
            print("You are out of chips. Please run the game again if you want to play some more!")
            break
        del deck, dealer, player
        continue
    else:
        break
