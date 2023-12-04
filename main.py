from art import logo
import os

print(logo)
print("Welcome to the secret auction program")

bids = {}

num_ppl = 'yes'
while num_ppl != 'no':
    name = input("What is your name?: ")
    try:
        bid = float(input("What is your bid?: $"))
    except ValueError:
        print("Invalid input. Please enter a numeric value")
    bids[name] = bid
    num_ppl = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    os.system("cls")
os.system("cls")


highest_bid = 0
highest_name = ""
for name, bid in bids.items():
    if bid > highest_bid:
        highest_name = name
        highest_bid = bid

print(f"The winner is {highest_name} with a bid of ${highest_bid}")
