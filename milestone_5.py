import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.current_lives = num_lives

        print(f"Word to guess: {' '.join(self.word_guessed)}")
        print(f"Number of lives: {self.current_lives}")

def check_guess(guess, word, word_guessed):
    guess = guess.lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid letter. Please, enter a single alphabetical character.")
        return None
    if guess in word:
        print(f"{guess} is in the word!")
        for i in range(len(word)):
            if word[i] == guess:
                word_guessed[i] = guess
    else:
        print(f"{guess} is not in the word.")
        return True
    return False

def ask_for_input(word, num_lives, word_guessed):
    while num_lives > 0 and '_' in word_guessed:
        guess = input("Guess a letter: ")
        guess = guess.lower()
        invalid_input = check_guess(guess, word, word_guessed)
        
        if invalid_input:
            num_lives -= 1
            print(f"You have {num_lives} lives left.")
        
        print(f"Word to guess: {' '.join(word_guessed)}")
        
    if num_lives == 0:
        print(f"Out of lives. The word was '{word}'.")
    else:
        print("Congratulations! You guessed the word.")

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.current_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            ask_for_input(game.word, game.current_lives, game.word_guessed)
        else:
            print('Congratulations. You won the game!')
            break

# List of words for the game
word_list = ["bananas","apples","grapes","strawberries","melons"]

# Play the game with the list of words
play_game(word_list)