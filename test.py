import random

num_1 = random.randint(1,10)
num_2 = random.randint(1,10)
num_3 = num_1 * num_2
print("Welcome! \n Answer the following question to score 1 point")
response = int(input(str(num_1) + "* ? = " + str(num_3)))
if response == num_2:
    print("Well done! You've earned 1 point")
else:
    print("That's the wrong answer")