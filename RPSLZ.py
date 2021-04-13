#modules imported
import random 

#main function used for playing the game
def gameInAction():
    print("Since you have choosen to play the game, You can choose between rock, paper, scissors, lizard and Spock")
    option = input("Type your repsonse here: ")
    option_upper = option.upper()
    if option_upper == "ROCK":
        AI_Choice()
        rock()
    elif option_upper == "PAPER":
        AI_Choice()
        paper()
    elif option_upper == "SCISSORS":
        AI_Choice()
        scissors()
    elif option_upper == "LIZARD":
        AI_Choice()
        lizard()
    elif option_upper == "SPOCK":
        AI_Choice()
        spock()
    else:
        print("invalid option please select a valid option.")


#introduction to the game
def play():
    choice = input("Would you like to play rock, paper, scissors, lizard, Spock? ")
    choice_upper = choice.upper()
    if choice_upper == "YES":
        gameInAction()
    else:
        print("Goodbye.")

#The random selcetion for the computer's option
def AI_Choice():
    option = random.randint(0,4)
    global outcome
    outcome = ""
    if option == 0:
        outcome = "ROCK"
    elif option == 1:
        outcome = "PAPER"
    elif option == 2:
        outcome = "SCISSORS"
    elif option == 3:
        outcome = "LIZARD"
    else:
        outcome = "SPOCK"
 #functions that determine the outcome based upon the users choice and the random choice of the computer        
def rock():
    print(f"You have choosen rock and the computer selected {outcome.lower()}")
    if outcome == "ROCK":
        print("It is a draw.")
    elif outcome == "PAPER":
        print("You lose.")
    elif outcome == "SCISSORS":
        print("You Win!")
    elif outcome == "LIZARD":
        print("You Win!")
    else:
        print("You lose.")
def paper():
    print(f"You have choosen paper and the computer selected {outcome.lower()}")
    if outcome == "ROCK":
        print("You Win!.")
    elif outcome == "PAPER":
        print("It is a draw.")
    elif outcome == "SCISSORS":
        print("You lose!")
    elif outcome == "LIZARD":
        print("You Win!")
    else:
        print("You lose.")
def scissors():
    print(f"You have choosen scissors and the computer selected {outcome.lower()}")
    if outcome == "ROCK":
        print("You lose.")
    elif outcome == "PAPER":
        print("You Win!")
    elif outcome == "SCISSORS":
        print("It is a draw")
    elif outcome == "LIZARD":
        print("You Win!")
    else:
        print("You lose")
def lizard():
    print(f"You have choosen lizard and the computer selected {outcome.lower()}")
    if outcome == "ROCK":
        print("You lose.")
    elif outcome == "PAPER":
        print("You lose.")
    elif outcome == "SCISSORS":
        print("You lose.")
    elif outcome == "LIZARD":
        print("It is a draw.")
    else:
        print("You Win!")
def spock():
    print(f"You have choosen Spock and the computer selected {outcome.lower()}")
    if outcome == "ROCK":
        print("You Win!")
    elif outcome == "PAPER":
        print("You Win!")
    elif outcome == "SCISSORS":
        print("You Win!")
    elif outcome == "LIZARD":
        print("You lose.")
    else:
        print("It is a draw")


play()
