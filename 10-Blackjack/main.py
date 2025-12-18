import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    return random.choice(cards)

def calculate_score(player_cards):
    score=0
    for card in player_cards:
        score += card
    return score

def compare(u_score,d_score):
    if u_score==d_score:
        return "Draw"
    elif u_score>21:
        return "you bust"
    elif d_score>21:
        return "dealer bust.so you win"
    elif u_score==21:
        return "you  win"
    elif d_score==21:
        return "you lose"
    elif u_score>d_score:
        return "you win"
    else:
        return "you lose"

def blackjack():
    print(art.logo)
    user_cards=[]
    dealer_cards=[]
    user_score=0
    dealer_score=0


    for i in range(2):
        user_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    game_over=False
    while not game_over:
        user_score=calculate_score(user_cards)
        dealer_score=calculate_score(dealer_cards)
        print(f"your cards: {user_cards} , current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if 11 in user_cards and user_score > 21:
            user_cards.remove(11)
            user_cards.append(1)

        if user_score==21 or dealer_score==21 or user_score>21:
            game_over=True
        else:
            want_card=input("Type 'y' to get another card, type 'n' to pass: ")
            if want_card=="y":
                user_cards.append(deal_card())

            elif want_card=="n":
                game_over=True

    while dealer_score<17 :
        dealer_cards.append(deal_card())
        dealer_score=calculate_score(dealer_cards)

    if 11 in dealer_cards and dealer_score>21:
        dealer_cards.remove(11)
        dealer_cards.append(1)

    print(f"your final hand: {user_cards}, your final score: {user_score}")
    print(f"Dealers final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score,dealer_score))

while input("you want to play Blackjack type 'y' for yes and 'n' for no: ")=='y':
    print("\n"*10)
    blackjack()
