#HERZING UNIVERSITY
#DBRANDUSA@HERZING.EDU
#UNIT1

#!/usr/bin/env python3

import random

def main():
  print ("Rock, Papers, Scissors")
  print ("----------------------")

  while True:
    user_input = input("\nEnter a choice (rock, paper, scissors): ")
    possible_choices = ["rock", "paper", "scissors"]
    result = random.choice(possible_choices)

    print(f"\nYou chose {user_input}, computer chose {result}.\n")

    if user_input == result:
        print(f"Both players selected {user_input}. It's a tie!")
    elif user_input == "rock":
        if result == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_input == "paper":
        if result == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_input == "scissors":
        if result == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    again = input("\nPlay again? (y/n): ")
    if again.lower() != "y":
        print("\nFine then, I didn't want to play with you anyways!\n")
        break

if __name__ == "__main__":
    main()