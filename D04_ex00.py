#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body

def guess_rand():
	#get a random integer
	x = random.randint(1,25)
	#initialize the guess
	y = ''
	#counter for guesses
	n = 1
	#while guess is less than 6 and while guess is not same as random int
	while y != x and n < 6:
		# ask the user for an input and say if its high/low/right
		# if wrong increment counter and ask for input again
		try:
			y = int(input("Guess a number"))
			if x == y:
				print ("Guess is right")
				break
			elif y > x:
				print ("Guess is too high") 
			else:
				print ("Guess is too low")
			n += 1	
		#exception for input values other than int
		except:
			n += 1 # increment counter
			if (n == 6):
				print ("Good luck next time")
			else:
				print("Try again")




################################################################################
def main():


    guess_rand() # Remove this and replace with your function calls
    

if __name__ == '__main__':
    main()