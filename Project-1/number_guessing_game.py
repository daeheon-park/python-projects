# Number Guessing Game : An integer between 1 and 100
# Keep track of the count : How many count it takes to guess the number.

import random

random_number = random.randint(1,100)
count = 0
choice = -1

while random_number != choice:
    choice = int(input("Guess the number : "))
    print("You're guess is wrong. Try again.")
    count += 1
    print(f"Number of trial : {count} ")
    if abs(random_number - choice) > 20:
        print("Your guess is way too different.") 
    elif abs(random_number - choice) <= 20 and abs(random_number - choice) > 10:
        print("Your guess is getting closer. Keep it up.")
    elif abs(random_number - choice) <= 10 and abs(random_number - choice) > 0:
        print("Getting closer! You're almost there.")
    elif random_number == choice:
        print(f"Well Guessed. '{choice}' is the correct answer.")
        break
        
print(f"The number of trial to guess the number is: {count}")


