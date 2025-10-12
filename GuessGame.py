import random
from colorama import Fore, init

init(autoreset=True)

class Game:
    def __init__(self, name="Game"):
        self.name = name

    def start(self):
        print(Fore.CYAN + f"Starting {self.name}...")

class GuessTheNumberGame(Game):
    def __init__(self):
        super().__init__("Guess The Number")
        self.max_number = 10
        self.correct_number = None

    def process_guess(self, guess):
        if guess > self.correct_number:
            print(Fore.RED + "Too high!")
        elif guess < self.correct_number:
            print(Fore.BLUE + "Too low!")
        else:
            print(Fore.GREEN + "Correct! You guessed it!")
        return True  # return True to indicate success
        return False  # guess was not correct


    def play(self):
        self.start()
        self.correct_number = random.randint(1, self.max_number)
        print(f"I'm thinking of a number between 1 and {self.max_number}.")
        attempts = 0

        while True:
            try:
                guess = int(input("Enter your guess: "))
                 # Invalid range → go to "Play Again"
                if guess < 1 or guess > self.max_number:
                    print(f"{Fore.YELLOW}Invalid guess! Please enter a number between 1 and {self.max_number}.")
                    break  # stop current game and jump to play again
                attempts += 1
                if guess < self.correct_number:
                    print(Fore.BLUE + "Too low!")
                elif guess > self.correct_number:
                    print(Fore.RED + "Too high!")
                else:
                    print(Fore.GREEN + f"Correct! You got it in {attempts} tries!")
                    break

            except ValueError:
                    print(Fore.YELLOW + "Invalid input! Please enter a valid integer.")
                    break  # invalid input also ends current game
if __name__ == "__main__":
    game = GuessTheNumberGame()
    while True:
        game.play()
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print(Fore.YELLOW + "Thanks for playing! 👋")
            break
