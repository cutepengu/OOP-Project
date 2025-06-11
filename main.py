import random
def show_intro():
    print("===================================")
    print("     WELCOME TO PUZZLE PALS!")
    print("===================================")
    print("Choose an option below.\n")

def add_currency(user_balance, amount):
    return user_balance + amount

def subtract_currency(user_balance, amount):
    if user_balance >= amount:
        return user_balance - amount
    
def generate_math_question():
        ("""Generates a random math question, gets user input, and provides feedback.""")

# displays the introduction when program is first opened
print("    WELCOME TO PUZZLE PALS") 
print("    Choose an option below.") 

# displays the options user can choose from
choices = int(input("""
                    1. Play Game
                    2. View Leaderboards
                    3. Help 
                    4. Exit Game 
                    """)) 

print(choices)
if choices == 1:
    # requests for year level to suit player's skills and requirements
    year_level = input("What is your year level?: ") 
    if year_level == 1:
        import random
        # generates random numbers and operator
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+"])

        # creates the question
        question = f"What is {num1} {operator} {num2}?"

            # calculates the correct answer
        if operator == "+":
              correct_answer = num1 + num2
        else:
          print("Error: Invalid operator")


            # gets user input
        user_answer = input(question + " ")
        try:
                # converted to float for accuracy
                user_answer = float(user_answer)
                if user_answer == correct_answer:
                    print("Correct!")
                else:
                     print(f"Incorrect. The answer is {correct_answer}.")
        except ValueError:
                print("Invalid input. Please enter a number.")

        # runs the function to generate a question
        generate_math_question()
       
    
    elif year_level == 2:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-"])
        
        # creates the question
        question = f"What is {num1} {operator} {num2}?"

        # calculates the correct answer
        if operator == "+":
          correct_answer = num1 + num2
        elif operator == "-":
          correct_answer = num1 - num2  
        else:
          print("Error: Invalid operator")


        # gets user input
        user_answer = input(question + " ")
        try:
        # converted to float for accuracy
            user_answer = float(user_answer)
            if user_answer == correct_answer:
                print("Correct!")
            else:
                print(f"Incorrect. The answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

            # runs the function to generate a question
            generate_math_question()

    elif year_level == 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-", "*"])
        
        # creates the question
        question = f"What is {num1} {operator} {num2}?"

        # calculates the correct answer
        if operator == "+":
          correct_answer = num1 + num2
        elif operator == "-":
          correct_answer = num1 - num2  
        elif operator == "*":
          correct_answer = num1 * num2
        else:
          print("Error: Invalid operator")


        # gets user input
        user_answer = input(question + " ")
        try:
        # converted to float for accuracy
            user_answer = float(user_answer)
            if user_answer == correct_answer:
                print("Correct!")
            else:
                print(f"Incorrect. The answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

            # runs the function to generate a question
            generate_math_question()


elif choices == 2:
    print()

elif choices == 3:
    print("Please choose the number of the option you require.")
    report = int(input("""
                       1. Report Player
                       2. Report Issue
                       3. Sound Control
                       """))
    if report == 1:
        print("Please tell us the player information of the player you would like to report and state the reason for your report: ")
        input("Player ID: ")
        input("Reason for Report: ")
        print("Thank you. We will work to our best to solve your issue.")

    elif report == 2:
        print("Please tell us the issue you would like for it to be solved. This can include anything we can improve on as well: ")
        input("Reason for Reporting an Issue: ")
        print("Thank you. We will work to our best to solve your issue.")

    elif report == 3:
        print("working on")
    else:
        print("Please choose a number from the options provided")
    
elif choices == 4:
    print("\nThanks for playing. Goodbye!\n")
else:
    print("Enter a number provided above.")

def show_Play_Game():
    print("\nPlay Game")
    print(" - Year Level: please enter your year level")
    print(" - Exit Game: exit the game\n")

def show_Leaderboards():
    print("\nLeaderboards:")
    print(" - Trophies")
    print(" - Wins")
    print(" - \n")

def show_help():
    print("\nHelp:")
    print(" - Sound Control: customise sound haptics")
    print(" - Report Player: Please tell us the player information of the player you would like to report and please state the reason for your report. Thank you.")
    print(" - Report Issue: Please tell us the issue you would like for it to be solved. This can include anything we can improve on as well. Thank you.")

def movement():
    print("\nPlayer moves north, east, south or west...\n")
