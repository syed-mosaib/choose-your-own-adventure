name= input("Type your name:")
print("Welcome", name, "to this adventure!")

answer = input("You are on dirt road, it has come to an end and you can go left or right:")

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim acccross? Type walk to walk around and swim to swim accross:  ")

    if answer == "swim":
        print("You swam accross and were eaten by an aalligator.")
    elif answer == "walk":
        print('You walked for many miles, ran out of a water and you lost the game.')
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)?:")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)?")

        if answer == "yes":
            print("You talk to the stranger and they give you gold, you win!")
        elif answer == "no":
            print("You talk to the stranger and they get offended, you lose.")
        else:
            print('Not a valid option. You lose.')
    
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for trying", name)   