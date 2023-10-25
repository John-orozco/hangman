
while True:
    guess = input("Guess a letter: ")

    if guess.isalpha() and len(guess) == 1:
        word="apple"
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
        break
    else:
        print("Invalid letter. Please enter a single alphabetical character.")