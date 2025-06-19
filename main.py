import random
player_1 = ''
player_2 = ''
# player class stores all the player information
class Player:

    # sets up player's information: name, year level, starting coins
    def __init__(self, player_name, year_level):
        self.player_name = player_name
        self.year_level = year_level
        self.coins = 0
        self.player_ID = str(random.randint(10000000, 99999999)) # provides each player an ID consisting of 8 numerical digits
        
        
    # adds coin to player's balance
    def add_coins(self, amount):
        self.coins += amount

    # subtracts coin from player's balance but cannot go below 0
    def subtract_coins(self, amount):
        self.coins = max(0, self.coins - amount)

# game class controls everything happening within the game
class Game:
      
    # sets up game with no player and empty leaderboard
    def __init__(self):
        self.player_name = None
        self.leaderboard = []  
        self.player_ID = set()

    # generates an 8 digit player id
    def generate_player_id(self):
        while True:
            new_ID = str(random.randint(10000000, 99999999))  # 8-digit number
            if new_ID not in self.used_IDs:
                self.used_IDs.add(new_ID)
                return new_ID 
            print(new_ID)

    # displays game title when it starts
    def show_intro(self):
        print("===================================")
        print("       WELCOME TO PUZZLE PALS!")
        print("===================================")

    # allows users to choose what to do: play game, view leaderboard, receive help, exit game
    def main_menu(self):
        while True:
            try:
                choice = int(input("""

1. Play Game
2. Play Multiplayer Game
3. View Leaderboards
4. Display Player ID
5. Help
6. Exit Game

Choose an option: """))

            except ValueError:
                print("Please enter a valid number.")
                continue

            # runs different parts of the game depending on user's choice
            if choice == 1:
                self.start_game() # runs game
            elif choice == 2:
                self.multiplayer_mode()
            elif choice == 3:
                try:
                    self.view_leaderboard() # displays leaderboard with name and amount of coins
                except:
                    print('You need to play a game first')
            elif choice == 4:
                try: 
                    
                    print(f"Your Player ID is: {player_1.player_ID}") # displays player's player ID
                except:
                    print('Play a game first please.')
            elif choice == 5:
                self.show_help() # displays options for help: report issue, report player, sound controls
            elif choice == 6:
                print("\nThanks for playing Puzzle Pals! See you next time!") # exits game
                break
            else:
                print("Please choose a number from 1 to 4.") # requests for a valid input

    # starts the game: gets player's name and year level
    def start_game(self):
        global player_1
        name = input("Enter your name: ")

        # repeats until a valid year level is entered
        while True:
            try:
                year = int(input("Enter your year level (1-12): "))
                if 1 <= year <= 12:
                    break
                else:
                    print("Year level must be between 1 and 12.")
            except ValueError:
                print("Please enter a number between 1 and 12.")

        # creates a new player object
        player_1 = Player(name, year)
        
        # moves on to the gameplay
        self.run_stage()

    # runs the stage of the game
    def run_stage(self):
        global player_1
        print(f"\nWelcome {player_1.player_name}!")
        print(f"Your Player ID is: {player_1.player_ID}")
        num_puzzles = 10

        # loops through each of the puzzles
        for i in range(1, num_puzzles + 1):
            print(f"\nPuzzle {i} of {num_puzzles}")
            self.ask_scaled_question(player_1)   

        print(f"\nGreat job, {player_1.player_name}! You finished all the puzzles.")
        print(f"You ended with {player_1.coins} coins.")

        self.leaderboard.append((player_1.player_name, player_1.coins))

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again == "yes":
            self.start_game()  # restart the game
        else:
            print("Returning to main menu...")

    # sets questions based on player's year level    
    def ask_scaled_question(self, player):
        global player_1
        year = player_1.year_level


        if year <= 4: 
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operator = random.choice(['+', '-'])

        elif year <= 8:
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            operator = random.choice(['+', '-', '*'])

        else:
            num1 = random.randint(1, 50)
            num2 = random.randint(1, 50)
            operator = random.choice(['+', '-', '*', '/'])

            if operator == '/':
                while num2 == 0 or num1 % num2 != 0:
                    num1 = random.randint(1, 50)
                    num2 = random.randint(1, 50)

        # calculates the correct answer
        if operator == '+':
            correct = num1 + num2
        elif operator == '-':
            correct = num1 - num2
        elif operator == '*':
            correct = num1 * num2
        elif operator == '/':
            correct = num1 // num2  # only whole number division in game

        try:
            # asks the question
            answer = int(input(f"What is {num1} {operator} {num2}? "))
            if answer == correct:
                print("Correct! You earn 10 coins.")
                player.add_coins(10)
            else:
                print(f"Incorrect. The correct answer was {correct}. You lose 5 coins.")
                player.subtract_coins(5)
        except ValueError:
            print("Invalid input. You lose 5 coins.")
            player.subtract_coins(5)

        # displays the updated amount of coins player has now
        print(f"Your current coin total is: {player.coins}")

    def multiplayer_mode(self):
        global player_1, player_2
        print("\n--- Multiplayer Mode ---")
        
        # get player 1 information
        name1 = input("Player 1, enter your name: ")
        while True:
            try:
                year1 = int(input("Player 1, enter your year level (1-12): "))
                if 1 <= year1 <= 12:
                    break
                else:
                    print("Year level must be between 1 and 12.")
            except ValueError:
                print("Please enter a number between 1 and 12.")
        player_1 = Player(name1, year1)
        
        # gets player 2 information
        name2 = input("Player 2, enter your name: ")
        while True:
            try:
                year2 = int(input("Player 2, enter your year level (1-12): "))
                if 1 <= year2 <= 12:
                    break
                else:
                    print("Year level must be between 1 and 12.")
            except ValueError:
                print("Please enter a number between 1 and 12.")
        player_2 = Player(name2, year2)

        # starts the game and displays both players' IDs
        print(f"\nWelcome {player_1.player_name} and {player_2.player_name}!")
        print(f"{player_1.player_name}'s Player ID: {player_1.player_ID}")
        print(f"{player_2.player_name}'s Player ID: {player_2.player_ID}")

        total_puzzles = 10
        puzzles_each = total_puzzles // 2 # fair distribution of questions

        # alternating turns between the two players
        for i in range(1, puzzles_each + 1):
            print(f"\nRound {i} - {player_1.player_name}'s turn")
            self.ask_scaled_question(player_1)

            print(f"\nRound {i} - {player_2.player_name}'s turn")
            self.ask_scaled_question(player_2)

        print("\n--- Game Over ---")
        print(f"{player_1.player_name} scored {player_1.coins} coins.")
        print(f"{player_2.player_name} scored {player_2.coins} coins.")

        # displays the outcome after the game ends
        if player_1.coins > player_2.coins:
            print(f"Congratulations {player_1.player_name}, you win!")
            self.leaderboard.append((player_1.player_name, player_1.coins))
        elif player_2.coins > player_1.coins:
            print(f"Congratulations {player_2.player_name}, you win!")
            self.leaderboard.append((player_2.player_name, player_2.coins))
        else:
            print("It's a tie!")
            self.leaderboard.append((player_1.player_name, player_1.coins))
            self.leaderboard.append((player_2.player_name, player_2.coins))

            input("Press Enter to return to the main menu.")

    # displays the list of top scores
    def view_leaderboard(self):
        print("\n=== Leaderboard ===")

        if not self.leaderboard:
            print("No scores yet!")
        else:
            # sorts the leaderboard from highest to lowest coins
            sorted_board = sorted(self.leaderboard, key=lambda x: x[1], reverse=True)
            for i, (name, coins) in enumerate(sorted_board, start=1):
                print(f"{i}. {name} - {coins} coins")

    # explains how the game works
    def show_help(self):
        help_choice = int(input("""

1. Report Player
2. Report Issue
3. Sound Controls

Choose an option: """)) 

        # allows player to report player
        if help_choice == 1: 
            print("Please provide us with the player ID of the person you would like to report and the reasoning for the report. Thank you.")
            report_player_ID = input("Player ID: ")
            report_reason = input("Reason of report: ")
            print("Thank you for your report. We will view it as quickly as possible.")
        # allows player to report game issue / system
        elif help_choice == 2:
            print("Please provide us with any issues regarding our game or our system. Thank you.")
            report_issue = input("Issues: ")
            print("Thank you for your report. We will view it as quickly as possible.")
        # allows player to toggle sound feature on and off  
        elif help_choice == 3: 
            sound_choice = int(input("""

1. Sound ON
2. Sound OFF

Choose an option: """)) 
            if sound_choice == 1:
                print("Sound turned on.")
            elif sound_choice == 2:
                print("Sound turned off")
            else:
                print("Please choose between 1 and 2.")

# Starts the whole game when the file runs
if __name__ == "__main__":
    game = Game()           # creates a new game object
    game.show_intro()       # displays welcome message
    game.main_menu()        # displays the main menu