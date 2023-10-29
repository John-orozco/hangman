import random

def check_guess(guess, word, word_guessed):
    guess = guess.lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid letter. Please, enter a single alphabetical character.")
        return None 
    if guess in word:
        print(f"{guess} is in the word!")
        # Update the word_guessed with the correct guess
        for i in range(len(word)):
            if word[i] == guess:
                word_guessed[i] = guess
    else:
        print(f"{guess} is not in the word.")
        return True  # Incorrect guess
    return False  # Correct guess

def ask_for_input(word, num_lives):
    word_guessed = ['_' for _ in word]
    while num_lives > 0:
        guess = input("Guess a letter: ")
        guess = guess.lower()
        incorrect_guess = check_guess(guess, word, word_guessed)
        
        if incorrect_guess:
            num_lives -= 1
            print(f"You have {num_lives} lives left.")
        
        print(f"Word to guess: {' '.join(word_guessed)}")
        
        if '_' not in word_guessed:
            print("Congratulations! You guessed the word.")
            break
        
    if num_lives == 0:
        print(f"Out of lives. The word was '{word}'.")

# Testing the code
word_to_guess = "apples"
ask_for_input(word_to_guess, num_lives=5)
