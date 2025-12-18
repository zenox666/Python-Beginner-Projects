
import random
import art
from game_data import data

def details(data_dict):
    name = data_dict['name']
    description = data_dict['description']
    country = data_dict['country']
    return f"{name}, a {description}, from {country}"


print(art.logo)

a_dict = random.choice(data)
data.remove(a_dict)
b_dict = random.choice(data)

score=0
game_over=False
while not game_over:

    print(f"Compare A: {details(a_dict)}")
    print(art.vs)
    print(f"Against B: {details(b_dict)}")

    a_followers=a_dict['follower_count']
    b_followers=b_dict['follower_count']

    your_answer = input("Who has more followers 'A' or 'B': ").lower()

    if your_answer=="a" and a_followers > b_followers:
        score += 1
        print("\n"*10)
        print(art.logo)
        print(f"You're Right! Current score: {score}")
        a_dict = b_dict
        data.remove(b_dict)
        b_dict = random.choice(data)

    elif your_answer=="b" and b_followers > a_followers:
        score += 1
        print("\n" * 10)
        print(art.logo)
        print(f"You're Right! Current score: {score}")
        a_dict = b_dict
        data.remove(b_dict)
        b_dict = random.choice(data)


    else:
        game_over = True
        print("\n"*10)
        print(art.logo)
        print(f"sorry that's wrong. Your Final score: {score}")

