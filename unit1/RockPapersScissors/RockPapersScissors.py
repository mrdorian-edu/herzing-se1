#HERZING UNIVERSITY
#DBRANDUSA@HERZING.EDU
#UNIT1

#!/usr/bin/env python3

import random

#game
def main():

  #title
  print ("Rock, Papers, Scissors")
  print ("-------------------------")

  #define variables
  playerScore = 0
  computerScore = 0
  tieScore = 0

  #loop until user ends the game
  while True:
    user_input = input("\nEnter a choice (rock, paper, scissors): ")
    possible_choices = ["rock", "paper", "scissors"]
    result = random.choice(possible_choices)

    print(f"\nYou chose {user_input}, computer chose {result}.\n")

    if user_input == result:
        print(f"Both players selected {user_input}. It's a tie!")
        tieScore += 1
    elif user_input == "rock":
        if result == "scissors":
            print("Rock smashes scissors! You win!")
            playerScore += 1
        else:
            print("Paper covers rock! You lose.")
            computerScore += 1
    elif user_input == "paper":
        if result == "rock":
            print("Paper covers rock! You win!")
            playerScore += 1
        else:
            print("Scissors cuts paper! You lose.")
            computerScore += 1
    elif user_input == "scissors":
        if result == "paper":
            print("Scissors cuts paper! You win!")
            playerScore += 1
        else:
            print("Rock smashes scissors! You lose.")
            computerScore += 1

    #current score
    print ("\nCurrent Score")
    print ("-------------------------")
    print ("You: " +str(playerScore)+ ", Computer: " +str(computerScore)+ ", Tie: " +str(tieScore)+"\n")

    again = input("> Play again? (y/n): ")

    if again.lower() != "y":
        print("\nFine then, I didn't want to play with you anyways!\n")
        break

if __name__ == "__main__":
    main()