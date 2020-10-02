#Black Jack

#Player play's aginst the computer (dealer), you are delt a card and then you will have the
#option to hit (be delt another card) or stand (stay with your current cards).
#If you go over 21 you bust (loose).
#If the dealer goes over 21 the dealer bust and you win granted you did not bust.

#Face card's are 10 points
#Numbered cards are worth their face value
#Ace's are 11 points

import random

print("Welcome to the game of Black Jack.")
name = input("Please Enter your name: ")
print("Hello " + name + " Are you ready to play? ")
choice = input()

def deal_cards():
    num = random.randint(2, 14)
    
    facecard = {2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
                    9: "Nine", 10: "Ten", 11: "Ace", 12: "Jack", 13: "Queen", 14: "King"}
    cardtype = facecard[num]
        
    cardpoints = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 10, 13: 10,
                    14: 10}
    cardvalue = cardpoints[num]

    return cardtype, cardvalue # returning a Tuple consisiting of two index

def game():
    player1points = 0
    player1choice = "hit"
    dealerpoints = 0
    dealerchoice = "hit"
    while player1points < 21 and player1choice.lower() == "hit":
        player1turn = deal_cards()
    
        print("player one has been delt a " + player1turn[0] + " worth " + str(player1turn[1]) + " points")

        player1points += player1turn[1]

        print("Player 1 now has " + str(player1points) + " points")

        if player1points == 21:
            break
        
        elif player1points > 21:
            print("Player 1 bust")
            break

        player1choice = input("Would player 1 like to hit or stay: ")

        if player1choice.lower() == "hit":
            deal_cards()

        elif player1choice.lower() == "stay":
            break

    while dealerpoints < 21 and dealerchoice.lower() == "hit":
        dealerturn = deal_cards()
    
        print("Dealer has been delt a " + dealerturn[0] + " worth " + str(dealerturn[1]) + " points")

        dealerpoints += dealerturn[1]

        print("Dealer now has " + str(dealerpoints) + " points")

        if dealerpoints == 21:
            break
        
        elif dealerpoints > 21:
            print("Dealer bust")
            break

        dealerchoice = input("Would Dealer like to hit or stay: ")

        if dealerchoice.lower() == "hit":
            deal_cards()

        elif dealerchoice.lower() == "stay":
            break

    if player1points > dealerpoints and player1points < 22:
        print("Player one has: " + str(player1points))
        print("Dealer has: " + str(dealerpoints))
        print("Player one wins")

    elif player1points < dealerpoints and dealerpoints < 22:
        print("Player one has: " + str(player1points))
        print("Dealer has: " + str(player2points))
        print("Dealer wins")

if choice.lower() == "yes":
    game()

else:
    print("Good bye")
