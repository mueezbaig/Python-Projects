print("Welcome to my computer Quiz!!!")

playing = input("Do you want to play?")

if playing.lower()!='yes':
    quit()
    
score = 0
print("Okay, let's start!")

answer = input("What does cpu stand for?")

if answer.lower() == 'central processing unit':
    print ("Correct!! ")
    score+=1

else:
    print("Incorrect!**")

answer = input("What does Gpu stand for?")

if answer.lower() == 'graphics processing unit':
    print ("Correct!! ")
    score+=1

else:
    print("Incorrect!**")

answer = input("What does RAM stand for?")

if answer.lower() == 'random access memory':
    print ("Correct!! ")
    score+=1

else:
    print("Incorrect!**")

answer = input("What does PSU stand for?")

if answer.lower() == 'power supply':
    print ("Correct!! ")
    score+=1

else:
    print("Incorrect!**")

print('You got '+ str(score)+ ' questions correct!')
print('You got '+ str((score/4)*100)+ '%.')