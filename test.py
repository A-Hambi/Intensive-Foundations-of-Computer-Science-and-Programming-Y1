import random
import operator

# Define a map of operations and their corresponding symbols
Symbols = {
    "Addition": (operator.add, "+"),
    "Subtraction": (operator.sub, "-"),
    "Multiplication": (operator.mul, "*"),
    "Division": (operator.truediv, "/")
}

# Generate a math question, prompt the user for an answer, and evaluate it
def generate_equation(operation, symbol, score):
    """
    Generates a math equation based on the symbol chosen 
    and checks the user's answer.

    Parameters:
        operation (function): The math operation (e.g., add, subtract).
        symbol (str): The symbol matching the operation (e.g., +, -, *, /).
        score (list): A mutable list storing the user's score.
    """
    # Generate random numbers for the equation
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)

    '''
    The numbers in the list ensure that the answer is doable without
    a calculator
    '''
    if operation == operator.truediv:
        num_1 = random.randint(10, 20)
        num_2 = random.choice([1, 2, 4, 5, 10])

    # Calculate the correct answer
    correct_answer = operation(num_1, num_2)

    # Randomly decide which part of the question to hide
    choice = random.randint(1, 3)

    # Generate the question string based on the choice
    if choice == 1:
        question = f"What is {num_1} {symbol} {num_2}?"
        expected = correct_answer
    elif choice == 2:
        question = f"What is ? {symbol} {num_2} = {correct_answer}?"
        expected = num_1
    elif choice == 3:
        question = f"What is {num_1} {symbol} ? = {correct_answer}?"
        expected = num_2

    # Output the question to the user and get their answer
    print(question)
    try:
        # Cast input as float for division, otherwise stay as integer
        user_response = (
            float(input("Your answer: "))
            if operation == operator.truediv
            else int(input("Your answer: "))
        )

        # Check if the user's answer is correct
        if user_response == expected:
            print("Correct! You've earned a point.")
            score[0] += 1  # Increment the score
        else:
            print(f"Incorrect. The correct answer was: {expected}")
    except ValueError:
        # Handle invalid input gracefully
        print(f"Invalid input! The correct answer was: {expected}")

# Welcome function to get the number of questions and type of questions
def welcome():
    """
    Prompts the user to input the number of questions 
    and the type of math questions they want.

    Returns:
        num_of_questions (int): The number of questions the user wants.
        question_type (int): The type of questions selected by the user.
    """
    while True:
        #Try statement to handle any non-integer inputs
        try:
            print("----- Maths Quiz -----")
            # Prompt for the number of questions
            num_of_questions = int(
                input("How many questions would you like to answer?"
                      "(1 - 10):\n")
            )
            #Loop to ensure user enters a number between 1 and 10
            while num_of_questions < 1 or num_of_questions > 10:
                print("Error: Please enter a number between 1 and 10")
                num_of_questions = int(
                    input("How many questions would you like to answer?"
                          "(1 - 10): \n")
                )

            # Prompt for the type of questions
            question_type = int(
                input(
                    "What type of questions would you like to answer?"
                    "\n1) Addition\n2) Subtraction\n3) Multiplication"
                    "\n4) Division\n5) Random\n"
                )
            )
        except ValueError:
            # Handle invalid input for integers
            print("Error: Please enter an integer")
            continue
        else:
            # Exit the loop if inputs are valid
            break

    return num_of_questions, question_type

# Main menu function to run the quiz
def main_menu():
    """
    Main function to run the math quiz. It prompts the user for inputs,
    generates questions, and keeps track of the score.
    """
    # Get the user preferences for the quiz
    num_of_questions, question_type = welcome()

    # Map user choices to operations and symbols
    question_map = {
        1: ("Addition", Symbols["Addition"]),
        2: ("Subtraction", Symbols["Subtraction"]),
        3: ("Multiplication", Symbols["Multiplication"]),
        4: ("Division", Symbols["Division"]),
        5: "Random"  # Special case for random question type
    }

    # Initialize score as a mutable list
    score = [0]

    # Loop through the desired number of questions
    for _ in range(num_of_questions):
        if question_type == 5:  # Handle random question type
            op_func, op_symbol = random.choice(list(Symbols.values()))
        else:
            # Validate the user's choice
            if question_type not in question_map:
                print("Invalid choice!")
                return
            # Extract the operation and symbol from the map
            op_func, op_symbol = question_map[question_type][1]

        # Generate and evaluate a question
        generate_equation(op_func, op_symbol, score)

    # Display the final score to the user
    print(f"Your final score is: {score[0]} out of {num_of_questions}")

# Run the main menu to start the quiz
main_menu()
