import art
import os
import platform
bid_list = []

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def bid_dict(bidder_name, bid_amount):
    bid_dictionary = {}
    bid_dictionary["name"] = bidder_name
    bid_dictionary["bid"] = bid_amount
    bid_list.append(bid_dictionary)

def bid_winner():
    winner_bid = bid_list[0]["bid"]
    winner_name = bid_list[0]["name"]
    for el in range(len(bid_list)):
        if winner_bid < bid_list[el]["bid"]:
            winner_bid = bid_list[el]["bid"]
            winner_name = bid_list[el]["name"]

    print(f"Congratulations {winner_name}, you are the winner, with a bid of ${winner_bid}.")

print(art.logo)
print("Welcome to the secret auction program.")
while True:
    name = input("What is your name ?: ")
    bid = int(input("What's your bid?: $"))
    bid_dict(name, bid)
    decision = input("Are there any other bidders? y/n: ")
    clear_console()
    if decision == 'y':
        print(art.logo)
        print("Welcome to the secret auction program.")
        continue
    else:
        bid_winner()
        break
