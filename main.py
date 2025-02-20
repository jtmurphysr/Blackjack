import random
import art

print(art.logo)

game_over = False

def create_deck():
    """Create a standard 52-card deck."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King', 'Ace']
    return [(rank, suit) for suit in suits for rank in ranks]


def shuffle_deck(deck):
    """Shuffle a deck of cards."""
    random.shuffle(deck)
    return deck

def deal_card(deck):
    """Deal one card from the deck."""
    return deck.pop()


def print_hand(hand):
    """Print a player's hand."""
    for card in hand:
        print(card[0], card[1])

def score_hand(hand):
    """Calculate the total score of cards in hand."""
    total = 0
    aces = 0

    for rank, _ in hand:
        if rank in ['Jack', 'Queen', 'King']:
            total += 10
        elif rank == 'Ace':
            total += 11
            ace_count += 1
        else:
            total += int(rank)


    # If total exceeds 21 and there's an ace, reduce its value from 11 to 1
    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total
    
def print_hand(hand, hide_first_card=False):
    """
    Print the cards in a hand.
    If hide_first_card is True, the first card is not revealed (used for the dealer).
    """
    if hide_first_card:
        print("Hidden Card")
        for card in hand[1:]:
            print(f"{card[0]} of {card[1]}")
    else:
        for card in hand:
            print(f"{card[0]} of {card[1]}")
    if not hide_first_card:
        print("Total value:", score_hand(hand))
    print()

def blackjack():
    #create and shuffle the deck
    deck = create_deck()
    deck = shuffle_deck(deck)
    # Deal initial hands
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    print("Dealer's Hand:")
    print_hand(dealer_hand, hide_first_card=True)

    print("Player's Hand:")
    print_hand(player_hand)

    #Player's turn
    while score_hand(player_hand) < 21:
        action = input("Type 'h' to hit or 's' to stand: ").lower()
        if action == 'h':
            player_hand.append(deal_card(deck))
            print("Player's Hand:")
            print_hand(player_hand)
            if score_hand(player_hand) > 21:
                print("You busted! Dealer wins.")
                game_over = True
                return
            elif score_hand(player_hand) == 21:
                print("Blackjack! You win!")
                game_over = True
                return
            else:
                continue
        elif action == 's':
            break
        else:
            print("Invalid action. Please try again.")

    #Dealer's turn
    print("Dealer's Turn:")
    print_hand(dealer_hand)
    while score_hand(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
        print("Dealer's Hand:")
        print_hand(dealer_hand)
        if score_hand(dealer_hand) > 21:
            print("Dealer busted! You win!")
            game_over = True
            return
        else:
            continue

    #Game Outcome
    print("\nFinal Results:")
    print(f"Dealer's Hand: {score_hand(dealer_hand)}")
    print(f"Player's Hand: {score_hand(player_hand)}")

    if score_hand(player_hand) == score_hand(dealer_hand):
        print("It's a draw!")
    elif score_hand(player_hand) > 21:
        print("You went over. You lose!")
    elif score_hand(dealer_hand) > 21:
        print("Dealer went over. You win!")
    elif score_hand(player_hand) > score_hand(dealer_hand):
        print("You win!")



blackjack()



