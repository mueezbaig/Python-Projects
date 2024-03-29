import random
import time

Operators = ["+","-","*"]
Min_Operators = 3
Max_Operators = 12
Total_Problems = 10

def generate_problem():
    left = random.randint(Min_Operators,Max_Operators)
    right = random.randint(Min_Operators,Max_Operators)
    op = random.choice(Operators)

    expr = str(left) + " " + op + " "+ str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start!")
print("---------------------")

start_time = time.time()

for i in range(Total_Problems):
    expr, answer = generate_problem()

    while True:
        guess = input("Problem #" + str(i+1) + ": " + expr + " = ")

        if guess == str(answer):
            break
        wrong+=1

end_time = time.time()
total_time = round(end_time - start_time,2)

print("---------------------")
print("Nice Work! You finished in", total_time, "seconds!")