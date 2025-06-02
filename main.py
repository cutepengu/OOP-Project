def show_intro():
    print("===================================")
    print("     WELCOME TO PUZZLE PALS!")
    print("===================================")
    print("Choose an option below.\n")

choices = int(input("""
                    1. Play Game
                    2. View Leaderboards
                    3. Help 
                    4. Exit Game 
                    """))

print(choices)
if choices == 1:
    input("What is your year level?: ")

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
