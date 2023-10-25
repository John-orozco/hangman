import random  
fruits_list = ["bananas","apples","grapes","strawberries","melons"]
random_fruit= random.choice(fruits_list)
print("Random Fruit Select:",random_fruit)
guess = input("Please enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")