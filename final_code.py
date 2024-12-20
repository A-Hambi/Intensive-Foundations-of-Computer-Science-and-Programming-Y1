import random

# Define the functions for each question type
def addition(score):
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    num_3 = num_1 + num_2
    choice = random.randint(1, 3)
    if choice == 1:
        question = f"What is {num_1} + {num_2}?"
        print(question)
        user_response = int(input("Your answer: "))
        if user_response == num_3:
            print("Correct! You've earned yourself a point.")
            score[0] += 1
        else:
            print(f"Incorrect. The correct answer was: {num_3}")
    elif choice == 2:
        question = f"What is ? + {num_2} = {num_3}?"
        print(question)
        user_response = int(input("Your answer: "))
        if user_response == num_1:
            print("Correct! You've earned yourself a point.")
            score[0] += 1
        else:
            print(f"Incorrect. The correct answer was: {num_1}")
    elif choice == 3:
        question = f"What is {num_1} + ? = {num_3}?"
        print(question)
        user_response = int(input("Your answer: "))
        if user_response == num_2:
            print("Correct! You've earned yourself a point.")
            score[0] += 1
        else:
            print(f"Incorrect. The correct answer was: {num_2}")
    return num_1, num_2, num_3

# Similar updates for subtraction, multiplication, and division functions
def subtraction(score):
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    num_3 = num_1 - num_2
    choice = random.randint(1, 3)
    if choice == 1:
        question = f"What is {num_1} - {num_2}?"
        print(question)
        user_response = int(input("Your answer: "))
        if user_response == num_3:
            print("Correct! You've earned yourself a point.")
            score[0] += 1
        else:
            print(f"Incorrect. The correct answer was: {num_3}")
    elif choice == 2:
        question = f"What is ? - {num_2} = {num_3}?"
        print(question)
        user_response = int(input("Your answer: "))
        if user_response == num_1:
            print("Correct! You've earned yourself a point.")
            score[0] += 1
        else:
            print(f"Incorrect. The correct answer was: {num_1}")
    elif choice == 3:
        question = f"What is {num_1} - ? = {num_3}?"
        print(question)
        user_response = int(input("Your answer: "))
        if user_response == num_2:
            print("Correct! You've earned yourself a point.")
            score[0] += 1
        else:
            print(f"Incorrect. The correct answer was: {num_2}")
    return num_1, num_2, num_3

def multiplication(score):
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    num_3 = num_1 * num_2
    choice = random.randint(1, 3)
    if choice == 1:
        question = f"What is {num_1} * {num_2}?"
        print(question)
        user_response = int(input("Your answer: "))
        if user_response == num_3:
            print("Correct! You've earned yourself a point.")
            score[0] += 1
        else:
            print(f"Incorrect. The correct answer was: {num_3}")
    elif choice == 2:
        question = f"What is ? * {num_2} = {num_3}?"
        print(question)
        user_response = int(input("Your answer: "))
        if user_response == num_1:
            print("Correct! You've earned yourself a point.")
            score[0] += 1
        else:
            print(f"Incorrect. The correct answer was: {num_1}")
    elif choice == 3:
        question = f"What is {num_1} * ? = {num_3}?"
        print(question)
        user_response = int(input("Your answer: "))
        if user_response == num_2:
            print("Correct! You've earned yourself a point.")
            score[0] += 1
        else:
            print(f"Incorrect. The correct answer was: {num_2}")
    return num_1, num_2, num_3

def division(score):
    num_1 = random.randint(10, 20)
    numbers = [1, 2, 4, 10]
    num_2 = random.choice(numbers)
    num_3 = num_1 / num_2
    choice = random.randint(1, 3)
    if choice == 1:
        question = f"What is {num_1} / {num_2}?"
        print(question)
        user_response = float(input("Your answer: "))
        if user_response == num_3:
            print("Correct! You've earned yourself a point.")
            score[0] += 1
        else:
            print(f"Incorrect. The correct answer was: {num_3}")
    elif choice == 2:
        question = f"What is ? / {num_2} = {num_3}?"
        print(question)
        user_response = int(input("Your answer: "))
        if user_response == num_1:
            print("Correct! You've earned yourself a point.")
            score[0] += 1
        else:
            print(f"Incorrect. The correct answer was: {num_1}")
    elif choice == 3:
        question = f"What is {num_1} / ? = {num_3}?"
        print(question)
        user_response = int(input("Your answer: "))
        if user_response == num_2:
            print("Correct! You've earned yourself a point.")
            score[0] += 1
        else:
            print(f"Incorrect. The correct answer was: {num_2}")
    return num_1, num_2, num_3

# Menu function
def menu():
    print("----- Maths Quiz -----")
    num_of_questions = int(input("How many questions would you like to answer? "))
    question_type = int(input("What type of questions would you like to answer? \n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Random\n"))
    return num_of_questions, question_type

# Main function
def main():
    num_of_questions, question_type = menu()

    question_map = {
        1: addition,
        2: subtraction,
        3: multiplication,
        4: division,
        5: lambda score: random.choice([addition, subtraction, multiplication, division])(score)
    }

    if question_type not in question_map:
        print("Invalid choice!")
        return

    score = [0]  # Mutable score list

    for _ in range(num_of_questions):
        question_map[question_type](score)

    print(f"Your final score is: {score[0]} out of {num_of_questions}")

main()
