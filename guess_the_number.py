#!usr/bin/python
'''
A very simple guess the number program

'''

from random import randint


random_number = randint(1,10)
print("I have a number, its between 1 and 10, Can you guess the number?")
    
while True:
    your_guess = input("Enter Guess: ")
    try:
        your_guess = int(your_guess)
        break
    except:
        print("Invalid, enter a number")
        continue
    
if random_number == your_guess:
    print("CORRECT, well done")
else:
    print("Not quite there, Try again")

	

