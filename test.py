import random
import operator

# Define Symbols map
Symbols = {
    "Addition": (operator.add, "+"),
    "Subtraction": (operator.sub, "-"),
    "Multiplication": (operator.mul, "*"),
    "Division": (operator.truediv, "/")
}

# Generate a question and evaluate the answer
def generate_equation(operation, symbol, score):
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    if operation == operator.truediv:  # Ensure division results in an integer
        num_1 = random.randint(10, 20)
        num_2 = random.choice([1, 2, 4, 5, 10])

    correct_answer = operation(num_1, num_2)
    choice = random.randint(1, 3)

    # Generate the question based on the choice
    if choice == 1:
        question = f"What is {num_1} {symbol} {num_2}?"
        expected = correct_answer
    elif choice == 2:
        question = f"What is ? {symbol} {num_2} = {correct_answer}?"
        expected = num_1
    elif choice == 3:
        question = f"What is {num_1} {symbol} ? = {correct_answer}?"
        expected = num_2

    print(question)
    try:
        user_response = float(input("Your answer: ")) if operation == operator.truediv else int(input("Your answer: "))
        if user_response == expected:
            print("Correct! You've earned a point.")
            score[0] += 1
        else:
            print(f"Incorrect. The correct answer was: {expected}")
    except ValueError:
        print(f"Invalid input! The correct answer was: {expected}")

# welcome function
def welcome():
    print("----- Maths Quiz -----")
    num_of_questions = int(input("How many questions would you like to answer? "))
    question_type = int(input(
        "What type of questions would you like to answer? \n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Random\n"))
    return num_of_questions, question_type

# main_menu function
def main_menu():
    num_of_questions, question_type = welcome()

    question_map = {
        1: ("Addition", Symbols["Addition"]),
        2: ("Subtraction", Symbols["Subtraction"]),
        3: ("Multiplication", Symbols["Multiplication"]),
        4: ("Division", Symbols["Division"]),
        5: "Random"
    }

    score = [0]  # Mutable score list

    for _ in range(num_of_questions):
        if question_type == 5:  # Random question
            op_func, op_symbol = random.choice(list(Symbols.values()))
        else:
            if question_type not in question_map:
                print("Invalid choice!")
                return
            op_func, op_symbol = question_map[question_type][1]

        generate_equation(op_func, op_symbol, score)

    print(f"Your final score is: {score[0]} out of {num_of_questions}")

main_menu()
