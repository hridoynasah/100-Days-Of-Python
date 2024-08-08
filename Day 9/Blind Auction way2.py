import art
import os
import platform
bid_dictionary = {}
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def bid_winner():
    highest_bid = 0
    winner = ""
    for key in bid_dictionary:
        if bid_dictionary[key] > highest_bid:
            highest_bid = bid_dictionary[key]
            winner = key

    print(f"Congratulations {winner}, you are the winner.With a bid of ${highest_bid}.")

print(art.logo)
print("Welcome to the secret auction program.")
while True:
    name = input("What is your name ?: ")
    bid_amount = int(input("What's your bid?: $"))
    bid_dictionary[name] = bid_amount
    decision = input("Are there any other bidders? y/n: ")
    clear_console()
    if decision == 'y':
        print(art.logo)
        print("Welcome to the secret auction program.")
    else:
        bid_winner()
        break