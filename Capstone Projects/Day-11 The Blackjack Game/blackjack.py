import random
import os

# ASCII art for cards
card_art = {
    2: """
 _____
|2    |
|  ♠  |
|____2|
""",
    3: """
 _____
|3    |
|  ♠  |
|____3|
""",
    4: """
 _____
|4    |
|  ♠  |
|____4|
""",
    5: """
 _____
|5    |
|  ♠  |
|____5|
""",
    6: """
 _____
|6    |
|  ♠  |
|____6|
""",
    7: """
 _____
|7    |
|  ♠  |
|____7|
""",
    8: """
 _____
|8    |
|  ♠  |
|____8|
""",
    9: """
 _____
|9    |
|  ♠  |
|____9|
""",
    10: """
 _____
|10  ♠|
|  ♠  |
|___10|
""",
    'J': """
 _____
|J    |
|  ♠  |
|____J|
""",
    'Q': """
 _____
|Q    |
|  ♠  |
|____Q|
""",
    'K': """
 _____
|K    |
|  ♠  |
|____K|
""",
    'A': """
 _____
|A    |
|  ♠  |
|____A|
"""
}

def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the score of a list of cards."""
    card_values = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    score = 0
    ace_count = 0
    for card in cards:
        if card in card_values:
            score += card_values[card]
            if card == 'A':
                ace_count += 1
        else:
            score += card
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1
    return score

def compare(user_score, computer_score):
    """Compares the user's score and the computer's score to determine the outcome."""
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def print_cards(cards, hidden=False):
    """Prints the cards in ASCII art."""
    if hidden:
        print(card_art['X'])
    for card in cards:
        print(card_art[card])

def play_blackjack():
    print("Welcome to Blackjack!")
    
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print("Your cards:")
        print_cards(user_cards)
        print(f"Your current score: {user_score}")
        
        print("Computer's first card:")
        print_cards([computer_cards[0]])
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                os.system('cls')
            else:
                os.system('cls')
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print("Your final hand:")
    print_cards(user_cards)
    print(f"Your final score: {user_score}")
    
    print("Computer's final hand:")
    print_cards(computer_cards)
    print(f"Computer's final score: {computer_score}")
    
    print(compare(user_score, computer_score))

if __name__ == "__main__":
    play_blackjack()
