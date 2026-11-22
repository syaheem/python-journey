# Week 2 - Lesson 2: Number Guessing Game
#
# Concepts:
# 1. 'while' loop (loops until a specific condition is met)
# 2. 'random' module (generating a secret random number)
# 3. 'break' statement (stopping a loop immediately)
# 4. State tracking (counting attempts)

import random

def main():
    number = []
    random_number_generated = random.randint(1,100)
    attempts = 0
    with open("random.txt","a") as file:
        file.write(f"{random_number_generated}\n")
    with open("random.txt","r") as file:
        for line in file:
            number.append(int(line.strip()))
        random_guess = random.randint(1,len(number))
        random_number = number[random_guess -1]
    

    while True:    
        guess = int(input(f"Enter a number for line {random_guess}:"))
        attempts += 1
        if guess > random_number:
            print("Too high")
        elif guess < random_number:
            print("Too low")
        else:
            print("gg bois")
            break

            
        
        

if __name__ == "__main__":
    main()
