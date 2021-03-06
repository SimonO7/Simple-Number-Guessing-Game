import random

'''
Simple number guessing game

The computer will choose a random number between 1 and 100, and the player has to guess what it is.
The computer will tell the player the range where the number is located between. 
The range will update after each round, using bisection search to determine the range.
'''

lower = 1
upper = 100
guesses = 0
answer = random.randint(lower, upper)

while True:
	guess = input("Guess the number between %d and %d: " % (lower,upper))
	
	try:
		guess = int(guess)
	except:
		print("Number not valid. Try again")
		continue
	
	if guess == answer:
		guesses += 1
		print("Correct! The number was:", answer)
		if guesses == 1:
			print("WOW! You guessed it in %d turn!" % guesses)
		else:
			print("You guessed it in %d turns!" % guesses)
		break
	elif guess >= lower and guess < answer:
		lower = guess
		guesses += 1
	elif guess <= upper and guess > answer:
		upper = guess
		guesses += 1
	else:
		print("Number out of bounds. Try again")
