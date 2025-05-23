import  art

print(art.logo)

dictionary = {}

while True :

    name = input("What is your name?")
    bid = input("What is your bid ? rs. ")

    dictionary[name] = bid

    choice = input("are there any other bidders? Type 'yes' or 'no'.").lower()

    if choice == "yes" :
        print("\n"*20)
        continue
    elif choice == "no" :
        name_winner = max(dictionary, key=dictionary.get)
        print(f"{name_winner} win the auction with a bid of {dictionary[name_winner]} Rs.")
        break
    else :
        print("invalid input")
        continue







