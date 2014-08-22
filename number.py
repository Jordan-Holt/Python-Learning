# I'm thinking of a number...game.

import random
import time

def introduction():
	print('Greetings.  What is your name?')
	participant = input()
	print()
	print('Well, ' + participant + ", you are in for") 
	print('the fight of your life.')
	#time.seconds(2)
	print()
	print('You are about to play a number guessing game.')
	print('However, you will choose your difficulty!')
	print()
	print('First, you will select the number')
	print('range for your quest.')
	print('This can be anywhere ')
	print('between 1 and 10,000.')
	print()
	return participant
	
def chooseRangeLow():
	print('Enter the lowest number in the range.')
	lowNumber = input()
	lowNumber = int(lowNumber)
	print()
	return lowNumber                            # Need conditions if input is not a number
	
def chooseRangeHigh():
	print('Enter the highest number in the range.')
	highNumber = int(input())
	print()
	return highNumber
	
def chooseAttempts():
	print ('Now choose the number of attempts you would like to challenge yourself with.')
	totalAttempts = int(input())
	print()
	return totalAttempts
	
participant = introduction()
lowNumber = chooseRangeLow()
while lowNumber < 1 or lowNumber > 9999:
	print ('I\'m sorry but your number is not within the given range. Please try again.')
	print()
	lowNumber = chooseRangeLow()

highNumber = chooseRangeHigh()
while highNumber < 1 or highNumber > 10000:   	# Makes sure high number is within given range.
	print ('I\'m sorry but your number is not within the given range. Please try again.')
	print()
	highNumber = chooseRangeHigh()
while highNumber <= lowNumber:					#Makes sure high number is larger than low number
	print("I'm sorry but your high number must be larger than your low number.  Please try again.")
	print()
	highNumber = chooseRangeHigh()
while highNumber - lowNumber == 1:				#Checks if anyone made a range of 1
	print("Way to challenge yourself, smart ass.  Give it another shot.")
	print()
	highNumber = chooseRangeHigh()

targetNumber = random.randint(lowNumber,highNumber)
totalAttempts = chooseAttempts()



totalGuesses = 0
while totalGuesses < totalAttempts:
	guessesRemaining = totalAttempts - totalGuesses
	if guessesRemaining > 1:
		print('You have %s guesses remaining. What is your guess?' % guessesRemaining)
	else:
		print('You have %s guess remaining. The pressure is on. What is your final guess?' % guessesRemaining)
	guess = input()
	print()
	if guess.isdigit():
		guess = int(guess)
		if guess < lowNumber or guess > highNumber:
			print("I'm sorry but your guess was outside of your range.  Please try again")
			print()
			continue
	else:
		print("I'm sorry, you didn't enter a numeric number. Please try again.")
		print()
		continue
	if guess > targetNumber:
		print('I am sorry but your guess is too high!')
		print()
	elif guess < targetNumber:
		print('I am sorry but your guess is too low!')
		print()
	else:
		print()
		break
	totalGuesses += 1
	
if guess == targetNumber:
	print('Congrats, ' + participant + ', you have guessed the correct number in ' + str(totalGuesses + 1) + ' attempts!')
	
else:
	print('I am sorry, ' + participant + ', you were not successful...this time...the correct number was ' + str(targetNumber) +'.')

input("Press Enter to Close")
		
		


	
			
			
		



























