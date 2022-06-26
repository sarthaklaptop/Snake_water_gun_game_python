import random

# Snake water gun OR Rock Water Scissor

def gameWin(comp, you):
    # If two values are equla there is a tie
    if comp == you:
        return None

    # Check for all possibilities when computer is s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    # Check for all possibilities when computer is w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    # Check for all possibilities when computer is g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print ("Computer's Turn: Snake(s) Water(w) or Gun(g)?")
randomNo = random.randint(1,3)
# print(randomNo)
if randomNo == 1:
    comp = 's'
elif randomNo == 2:
    comp = 'w'
elif randomNo == 3:
    comp = 'g'

you = input("Your's Turn: Snake(s) Water(w) or Gun(g)?\n")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is tye")
    # pass
elif a:
    print("You Win")
else:
    print("You Loose")
