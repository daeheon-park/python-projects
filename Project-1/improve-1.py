# 1) Avoid repeating same sentences : 
# I Used "abs(random_number - choice)" for 4 times. 
# It would be better if I create a new variable and make it simple.

# 2) Count only valid guess :
# int(input()) will crash if the user types like "abc"
# use try/except and continue so invalid inputs don't count as attempts/

import random
random_number = random.randint(1,100)
count = 0

while True:
    try:
        choice = int(input("Guess the number (1~100) : "))
    except ValueError: # Prevent crashing the program
        print("Please enter an integer.")
        continue

    if not (1<= choice <= 100):
        print("Out of range. Guess between 1 and 100.")
        continue

    count += 1
    diff = abs(random_number - choice)

    if choice == random_number: # consider the correct statement first.
        print(f"Well guessed! {choice} is the correct answer.")
        break

    print("Your guess is wrong. Try again.")
    print(f"Number of trials: {count}")

    if diff > 20:
        print("Your guess is way too different.")
    elif diff <= 20 and diff > 10:
        print("You are getting closer. Keep it up.")
    elif diff <= 10 and diff >= 1:
        print("You are almost there! Try your luck.")

print(f"The number of trials to guess the number is : {count}.")