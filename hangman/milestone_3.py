
def check_guess(guess, word):
    guess = guess.lower()
    if guess in word:
        print(f"{guess} is in the word!")
    else:
        print(f"{guess} is not in the word.")

def ask_for_input(word):
    while True:
        guess = input("Guess a letter: ")
        guess = guess.lower()
        check_guess(guess, word)

        play_again = input("Do you want to guess another letter? (y/n): ")
        if play_again.lower() != "y":
            break

word_to_guess = "apples"
ask_for_input(word_to_guess)