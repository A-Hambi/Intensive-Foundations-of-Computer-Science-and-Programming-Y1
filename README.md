# Intensive-Foundations-of-Computer-Science-and-Programming-Y1
---
## User Manual:
### **Overview**
The Maths Quiz program is an interactive tool designed to help users practice simple arithmetic equations. It generates random math questions, checks user answers, and provides feedback on accuracy. Users can tailor their experience by selecting the number of questions they would like to answer and choose specific types of operations or a random selection.
## *Getting Started*
### Requirements
*	A computer with Python installed (version 3.6 or later).
*	A terminal or command-line interface to run the program.
### Running the Program
1.	Save the program file (e.g., maths_quiz.py) to your computer.
2.	Open a terminal or command prompt.
3.	Navigate to the directory where the program is saved.
4.	Run the program by typing:	python maths_quiz.py
5.	Follow the on-screen instructions.
### Using the Program
**Main Menu**
Upon starting the program, the user will see:  
1. ![Screenshot 2024-12-25 161145](https://github.com/user-attachments/assets/622dc3af-ac1e-4f7e-9dcf-2e2a0e2f8fe4)  
If you enter a number outside this range, you’ll be prompted to try again.  
2. ![Screenshot 2024-12-25 161248](https://github.com/user-attachments/assets/4202a2c7-6000-404c-b275-a95394bd2029)  
**Question Type**: Choose the type of arithmetic questions by entering a number:  
*	1 for Addition
*	2 for Subtraction
*	3 for Multiplication
*	4 for Division
*	5 for a random mix of all question types  
3. ![Screenshot 2024-12-25 161428](https://github.com/user-attachments/assets/3b36eb4c-f2af-463a-a906-35af6630583b)  
**User Response**: Here is an example of what a question will look like. Enter a number followed by the enter key to submit your answer.  
### Answering Questions
*	For each question, type your answer when prompted and press Enter.
*	The program will indicate whether your answer is correct and update your score.
*	If you input an invalid response (e.g., letters or special characters), the program will display the correct answer and proceed to the next question.
### Final Score
At the end of the quiz, your total score is displayed:
*	Example: “Your final score is: 7 out of 10”
### Quitting the Program
You can exit the program at any time by pressing Ctrl+C in the terminal.
### Tips for Success
*	For division questions, expect numbers that divide evenly for simplicity.
*	Pay attention to the format of questions (e.g., missing numbers or complete equations).
*	Use the random option (5) for a range of challenging questions.
---
## Technical Documentation:
### **Program Structure**
The Maths Quiz program consists of the following main components:

### 1. Symbol Mapping
The Symbols dictionary maps operation names to built-in Python functions and their corresponding mathematical symbols. It includes operations like addition, subtraction, multiplication, and division, and serves as the backbone for generating equations dynamically. This modular approach simplifies the integration of additional operations in the future, such as exponentiation or modulus.  
![Screenshot 2024-12-25 153401](https://github.com/user-attachments/assets/dfbf3a69-365c-46c7-bcc9-49356a648651)  
* **Purpose**: Simplifies dynamic question generation and allows easy addition of new operations.  
### 2. Functions
**a) generate_equation**
*	**Purpose:** Creates a math question tailored to the user-selected operation and evaluates responses.
*	**Parameters:**
	- operation: A function reference for the arithmetic operation (e.g., operator.add).
	- symbol: A string representing the operation (e.g., "+").
	- score: A mutable list to store the user's current score.
*	**Details:**
	- Randomly generates two integers within a predefined range (e.g., 1–10).
	- For division, ensures results are whole numbers by constraining the operands.
	- Hides either an operand or the result to create varied question formats.
	- Validates inputs to handle invalid responses gracefully, displaying the correct answer when necessary.
**b) welcome**
*	**Purpose:** Collects and validates the user's preferences for the quiz.
*	**Details:**
	- Prompts the user to select the number of questions (1–10).
	- Ensures input is an integer within the range; invalid inputs trigger an error message.
	- Offers choices for question types, leveraging the Symbols dictionary for streamlined mapping.
	- Returns validated preferences for use in subsequent functions.
### 3. Program Flow
1.	**Initialization:** The program starts by importing required modules (random, operator) and defining the Symbols dictionary.
2.	**Main Menu:** The main_menu function orchestrates user input collection, question generation, and scoring.
3.	**Question Generation:** For each question, the program:
	- Randomly generates operands.
	- Constructs a question string.
	- Evaluates the user’s response.
4.	**Final Output:** After all questions are answered, the program displays the user’s score.
### Error Handling
1.	**Invalid Input:**
	- Non-integer inputs for the number of questions or question type trigger a ValueError.
	- The program displays an error message and prompts the user to try again.
2.	**Out-of-Range Values:**
	- Inputs outside the valid range (e.g., more than 10 questions) prompt a retry.
3.	**Unexpected Errors:**
	- Invalid answers (e.g., letters) result in the correct answer being displayed, and the quiz continues.
### Key Design Considerations
*	**Modularity:** Each function performs a specific task, promoting reusability and readability.
*	**User Experience:** Clear instructions and error messages ensure ease of use.
*	**Scalability:** The Symbols dictionary allows for easy extension with new operations.
## Testing and Validation
*	**Functional Testing:** Verified all arithmetic operations and question formats.
*	**Boundary Testing:** Checked limits (e.g., 1 and 10 questions, valid/invalid inputs).
*	**Error Recovery:** Ensured graceful handling of invalid inputs without program crashes.
---
### Future Improvements
1.	**Advanced Question Types:** Introduce parentheses or multi-step problems.
2.	**Difficulty Levels:** Allow users to select difficulty, adjusting operand ranges.
3.	**Score Persistence:** Save scores across sessions for progress tracking.
4.	**Graphical Interface:** Develop a GUI for an enhanced user experience.
---
