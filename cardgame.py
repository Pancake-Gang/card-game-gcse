import random
import time
import pandas as pd

authorised_user = ["Jin", "Jacky", "Kyle", "Winnie", "Peniel"]

deck = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10",
        "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "Y10",
        "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]

player1_cards = []
player2_cards = []
player1_winning_deck = []
player2_winning_deck = []

current_card1 = ""
current_card2 = ""
random.shuffle(deck)

def authorisation(player):
    if player in authorised_user:
        print(f"Welcome to the game, {player}!")
    else:
        print(f"Sorry {player}, you are not authorised to play this game.")

player1 = input("Enter first player's username: ")
authorisation(player1)
if player1 in authorised_user:
    player2 = input("Enter second player's username: ")
    authorisation(player2)
    print("")

def deal_cards(player_deck):
    player_deck.append(deck[0])
    deck.pop(0)

def tied_colour():
    global player1_score
    global player2_score
    #CNN is Current Card Number
    if len(current_card1) == 3:
        player1_CCN = current_card1[1] + current_card1[2]
    else:
        player1_CCN = current_card1[1]

    if len(current_card2) == 3:
        player2_CCN = current_card2[1] + current_card2[2]
    else:
        player2_CCN = current_card2[1]

    player1_CCN = int(player1_CCN)
    player2_CCN = int(player2_CCN)

    if player1_CCN > player2_CCN:
        print(f"{player1} Won!")
        player1_winning_deck.append(current_card1)
        player1_winning_deck.append(current_card2)
    else:
        print(f"{player2} Won!")
        player2_winning_deck.append(current_card1)
        player2_winning_deck.append(current_card2)


if player1 in authorised_user and player2 in authorised_user:

    for i in range(0,15):

        deal_cards(player1_cards)
        deal_cards(player2_cards)

        current_card1 = player1_cards[i]
        Colour_card1 = current_card1[0]

        current_card2 = player2_cards[i]
        Colour_card2 = current_card2[0]


        if (Colour_card1 == "R" and Colour_card2 == "B") or \
           (Colour_card1 == "Y" and Colour_card2 == "R") or \
           (Colour_card1 == "B" and Colour_card2 == "Y"):
            print(f"{player1} Won!")
            player1_winning_deck.append(current_card1)
            player1_winning_deck.append(current_card2)
        elif (Colour_card2 == "R" and Colour_card1 == "B") or \
           (Colour_card2 == "Y" and Colour_card1 == "R") or \
           (Colour_card2 == "B" and Colour_card1 == "Y"):
            print(f"{player2} Won!")
            player2_winning_deck.append(current_card1)
            player2_winning_deck.append(current_card2)
        else:
            print("The colour is tied!")
            tied_colour()

    print("")
    if len(player1_winning_deck) > len(player2_winning_deck):
        print(f"{player1} won the game!\n")
        print(f"The cards of {player1}'s deck: \n{player1_winning_deck}")

        file = open("winners.csv", "a")
        file.write(f"{player1}, {len(player1_winning_deck)}\n")
        file.close()

    else:
        print(f"{player2} won the game!\n")
        print(f"The cards of {player2}'s deck: \n{player2_winning_deck}")

        file = open("winners.csv", "a")
        file.write(f"{player2}, {len(player2_winning_deck)}\n")
        file.close()


    DataFrame = pd.read_csv('winners.csv')
    
    DataFrame.sort_values(
        by="Card Amount",
        axis=0,
        ascending=[False],
        inplace=True
    )
    print("")
    print(" --- Top 5 highest scores --- ")
    print(DataFrame.head())