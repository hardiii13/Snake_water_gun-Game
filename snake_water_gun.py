import random
lst=['S','W','G']

Total_chances=10
no_of_chances=0
computer_point=0
human_point=0

print("Snake, Water, Gun  Game")
print("S for snake \n W for water \n G for gun \n ")

#making the game in while loop
while no_of_chances<Total_chances:
    spin1=input("Snake,water,gun:")
    _random=random.choice(lst)                    #chooses one option randomly out of the list

    if spin1== _random:
        print("Tie both got 0 points")
    #if user enters s

    elif spin1== "S" and _random == "G":
        computer_point=computer_point+1
        print(f"your guess {spin1} and computer guess is {_random} \n")
        print("Computer wins one point \n")
        print(f"computers point is {computer_point} and human point is {human_point} \n")

    elif spin1=="S" and _random=="W":
        human_point=human_point+1
        print(f"your guess {spin1} and computer guess is {_random} \n")
        print("Human wins one point \n")
        print(f"Computer point is {computer_point} and human point is {human_point} \n")

    #if user enters w

    elif spin1== "W" and _random== "S":
        computer_point=computer_point+1
        print(f"your guess {spin1} and computer guess is {_random} \n")
        print("Computer wins one point \n")
        print(f"computer point is {computer_point} and human point is {human_point} \n")

    elif spin1=="W" and _random== "G":
        human_point=human_point+1
        print(f"your guess{spin1} and computer guess is {_random}  \n")
        print("human wins one point \n")
        print(f"Computer point is {computer_point} and human point is {_random} \n")

    #if user enter g

    elif spin1=="G" and _random == "S":
        human_point=human_point+1
        print(f"your guess {spin1} and computer guess is {_random} \n")
        print("human wins one point")
        print(f"computer point is {spin1} and human point is {human_point} \n")

    elif spin1=="G" and _random == "W":
        computer_point=computer_point+1
        print(f"your guess {spin1} and computer guess {_random}\n")
        print("computer wins one point")
        print(f"computer point is {computer_point} and human point is {human_point} \n")


    else:
        print("you have entered wrong input")

    no_of_chances=no_of_chances+1
    print(f"{Total_chances-no_of_chances} chances  are left out of {Total_chances} \n")

print("GAME OVER")
if human_point>computer_point:
    print("Human is the winner")
elif computer_point>human_point:
    print("Computer is the winner")
else:
    print("The match is tie no one is the winnner")

print(f"your point is {human_point} and computer point is {computer_point}")

