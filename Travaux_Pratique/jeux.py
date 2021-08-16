from replit import clear
#from art import logo

# HINT: You can call clear() to clear the output in the console.
#print(logo)
print("Welcom to the secret auction program")

secret_auction = {}
continue_play = True
highest_bid = 0
winner = ""

while  continue_play:
    name = input("What is your name ?: ")
    bid = int(input("What is your bid ?: $"))
    secret_auction[name] = bid

    choice = input("Are there any other bidders ? type 'yes' or 'no': \n").lower()
    if choice == "no":
        continue_play = False
    elif choice == "yes":
        clear()

for person in secret_auction:
    money_bet = secret_auction[person]
    if money_bet > highest_bid:
        highest_bid = money_bet
        winner = person
print(f"The winner ist {winner} with a bid of $ {highest_bid}")
