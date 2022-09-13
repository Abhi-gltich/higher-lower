from art import vs, logo  
from data import data
import random

def generate_random_acc():
    return random.choice(data)

def manage_data(acc):
    name = acc["name"] 
    description = acc["description"]  
    country = acc["country"]  

    return f"{name} is a {description} in {country}."

def compare(follower_count1, follower_count2):
    if follower_count1 > follower_count2:
        return "a"
    elif follower_count2 > follower_count1:
        return "b"
    
def game():
    play = True
    total = 0
    print(logo)
    account2 = generate_random_acc()
    while play:
        account1 = account2
        
        while account1 == account2:
            account2 = generate_random_acc()

        follower_count1 = account1["follower_count"]
        follower_count2 = account2["follower_count"]

        print( "Compare A:",manage_data(account1))
        print(vs)
        print("With B:",manage_data(account2))

        user_guess = input("Who has more followers? Press A or B. \n").lower()
        answer = compare(follower_count1, follower_count2)

        if answer == user_guess: 
            total += 1
            print(f"Correct, your score is {total}")
            play = True
        elif answer != user_guess:
            print(f"Wrong, you lose\nYour total is {total}")
            play = False
        

game()
