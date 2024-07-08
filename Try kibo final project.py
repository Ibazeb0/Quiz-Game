# Quiz about Anthony Ibazebo second year student

# List for questions, options and answers
questions = [
    "What is Anthony's current level in Computer Science?",
    "Which position did Anthony serve in NACOS Crawford Chapter?",
    "What is Anthony's current GPA?",
    "What role does Anthony currently hold in CUDaLS?",
    "Which company did Anthony work for as a Virtual Assistant?",
    "Which role did Anthony achieve after being a Social Media Manager?"
]

choices = [
    ["100 level", "200 level", "300 level", "400 level"],
    ["President", "Vice President", "Public Relations Officer", "Secretary"],
    ["Second class lower", "Second class upper", "First class", "Third class"],
    ["President", "Vice President", "Treasurer", "Member"],
    ["Google", "Supernar", "Amazon", "Facebook"],
    ["CEO", "CTO", "Head of Social Media team", "Marketing Director"]
]

answers = [
    "200 level", "Public Relations Officer", "First class", "Vice President",
    "Supernar", "Head of Social Media team"
]

# Running the quiz
score = 0  # Initializing the score

for i in range(len(questions)):  # Looping through the questions
    print(questions[i])
    for j in range(len(choices[i])):  # Looping through the options
        print(f"{j + 1}. {choices[i][j]}")

    while True:  # Looping until the user enters a valid input
        try:
            user_input = int(input("Enter the number of your choice: "))
            if user_input < 1 or user_input > 4:
                print("Invalid choice, please enter a number between 1 and 4.")
            else:
                break
        except ValueError:
            print("Invalid input, please enter a number.")

    if choices[i][user_input -
                  1] == answers[i]:  # Checking if the answer is correct
        print("Correct!\n")
        score += 1  # Incrementing the score
    else:
        print(f"Wrong! The correct answer is: {answers[i]}\n")

print(f"Your final score is {score} out of {len(questions)}"
      )  # Printing the final score
