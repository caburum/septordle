from random import choice
from numpy import loadtxt
from sys import stdout

def printRed(text):
	print('\033[91m', text, '\033[00m', sep='', end='')
def printGreen(text):
	print('\033[92m', text, '\033[00m', sep='', end='')
def printYellow(text):
	print('\033[93m', text, '\033[00m', sep='', end='')
def clearLine():
	stdout.write('\033[F\033[K')

words = loadtxt('words.txt', dtype=str)

word = choice(words).lower()
print(word)
print()

print('guess a 7-letter word:')
print('_______')

guessed = False

for _ in range(6):
	guess = input('').lower()

	clearLine()

	if not (len(guess) == 7 and guess in words):
		print(u'\u0336'.join(guess) + u'\u0336' + ' (invalid)')
		continue

	# we'll remove letters from here so we don't tell the user there are more of a letter than there are
	tempWord = word

	for i in range(7):
		letter = guess[i]
		if word[i] == letter:
			printGreen(letter)
		elif letter in tempWord:
			printYellow(letter)
		else:
			printRed(letter)
		tempWord = tempWord.replace(letter, '', 1)
	print() # end line

	if guess == word:
		guessed = True
		break

if guessed:
	print('you guessed the word correctly')
else:
	print('the word was', word)