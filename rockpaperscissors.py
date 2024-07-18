import random


def game():
    rules = ["paper","scissors","stone"]

    user = input("Which action would you like to use:\nPaper\nScissors\nStone\nPlay here: ")

    robot = random.choice(rules)
    if user == "paper" and robot == "stone" or user == "scissors" and robot == "paper" or user == "stone" and robot == "scissors":
        print(f"You won! You picked: {user}. Robot picked: {robot}")
    elif user == "stone" and robot == "paper" or user == "paper" and robot == "scissors" or user == "scissors" and robot == "stone":
        print(f"Robot won!Robot picked: {robot}. You picked: {user}")
    else:
        print("DRAW!")
def main():
    while True:
        print("""Welcome to the rock paper scissors!""")
        user_input = int(input("Press\n1. Play\n2.Exit\n"))
        if user_input == 1:
            game()
        elif user_input == 2:
            print("Exiting...\n")
            break

main()