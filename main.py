import random

def generate_equation():
    num_1 = random.randint(1,10)
    num_2 = random.randint(1,10)
    num_3 = num_1 * num_2
    return(num_1,num_2,num_3)
   
score = 0

for i in range(10):
    choice = random.randint(1,2)
    num_1,num_2,num_3 = generate_equation()
    if choice == 1:
        question = "what is " + str(num_1) + "*" + str(num_2) + "?"
        print(question)
        user_response = int(input("Your answer: "))
        if user_response == num_3:
            print("Correct! You've earned yourself a point")
            score += 1
        else:
            incorrect_answer = "That wasn't the number we were looking for. \n The correct answer was:  " + str(num_3)
            print(incorrect_answer)
    else:
        question = "what is " + str(num_1) + "* ? = " + str(num_3)
        print(question)
        user_response = int(input("Your answer: "))
        if user_response == num_2:
            print("Correct! You've earned yourself a point")
            score += 1
        else:
            incorrect_answer = "That wasn't the number we were looking for. \n The correct answer was:  " + str(num_3)
            print(incorrect_answer)
    

user_score = "Your final score is:  " + str(score) + " out of 10"
print (user_score)