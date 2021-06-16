import random
def game(computer, player):
    if computer == player:
        return None
    elif computer == "st" and player == "p":
        return True
    elif computer == "st" and player == "sc":
        return False
    elif computer == "p" and player == "st":
        return False
    elif computer == "p" and player == "sc":
        return True
    elif computer == "sc" and player == "st":
        return True
    elif computer == "sc" and player == "p":
        return False

print("\nComputer has choosen his choice and now it is your turn\n")
randNo = random.randint(1, 3)
if randNo == 1:
    computer = "st"
elif randNo == 2:
    computer = "p"
elif randNo == 3:
    computer = "sc"

player = input("Enter here, Stone(st), Paper(p) or Scissor(sc)?\n")
if computer == "st":
    print("The Computer has choosen Stone\n")
elif computer == "p":
    print("The computer has choosen Paper\n")
elif computer == "sc":
    print("The computer has choosen Scissor\n")
if player == "st":
    print("You have choosen Stone\n")
elif player == "p":
    print("You have choosen Paper\n")
elif player == "sc":
    print("You have chooen Scissor\n")

a = game(computer, player)
if a == None:
    print("The game has tied\n")
elif a == True:
    print("Congratulations!! You Won!")
elif a == False:
    print("Sorry, You Loose.\n")