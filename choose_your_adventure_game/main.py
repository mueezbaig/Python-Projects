name = input("Type your name: ")
print("welcome",name, "to this adventure!!")

answer = input("you are on a dirt road, it has come to an end and you can go left or right. which way would you like to go (left/right)? ").lower()

if answer == 'left':
    answer = input("you came to a river , you can walk aroud it or swim across (swim/walk)? ")

    if answer == 'swim':
        print('You  swam across and were eaten by alligator. ')
    
    elif answer == 'walk':
        print('You walked for many miles, ran out of water and you lost the game!')
    
    else:
        print('Not a valid option!!!')

elif answer == 'right':
    answer = input("You come to a bridge, it looks woobly, do you want to cross it  or head back (cross/back)?")

    if answer == 'back':
        print('You go back and loose!!!')
    
    elif answer == 'cross':
        print('Finally you cross the Bridge...')
        print('Congrats!!! You Won the game')
    
    else:
        print('Not a valid option!!!')
else:
    print('Not a valid option!!!')