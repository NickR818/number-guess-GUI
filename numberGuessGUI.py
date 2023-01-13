"""
1/6/2023 Program: numberGuessGUI.py
Template code for all GUI-based applications
NOTE: The file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""
from breezypythongui import EasyFrame
import random
# other imports can go here
class GuessingGame(EasyFrame):
	# definiton of the __init__() method which is out class constructor
	def __init__(self):
		# call the EasyFrame constructor method
		EasyFrame.__init__(self, title = "Guessing Game", width = 240, height = 180)
		# initialize the instance variables for the class
		self.magicNum = random.randint(1, 100)
		self.count = 0
		# create and add widgets to the window
		self.hintLabel = self.addLabel(text ="Guess a number between 1 and 100", row = 0, column = 0, columnspan = 2, sticky = "NSEW")
		self.addLabel(text = "Your guess:", row = 1, column = 0)
		self.guessField = self.addIntegerField(value = 0, row = 1, column = 1)
		self.guessButton = self.addButton(text = "Guess", row = 2, column = 0, command = self.nextGuess)
		self.newButton = self.addButton(text = "New Game", row = 2, column = 1, command = self.newGame)
	# definition of the event handling methods for this class
	def nextGuess(self):
		""" processes the user's next guess """
		self.count += 1
		guess = self.guessField.getNumber()
		# logic that determines the game's outcome
		if guess < self.magicNum:
			self.hintLabel["text"] = "Sorry, your guess was too small!"
		elif guess > self.magicNum:
			self.hintLabel["text"] = "Sorry, your guess was too large!"
		else:
			self.hintLabel["text"] = "Congratulations! You got it in " + str(self.count) + " tries!"
			self.guessButton["state"] = "disabled"
	def newGame(self):
		""" resets the data and GUI back to their original states """
		self.magicNum = random.randint(1, 100)
		self.count = 0
		self.guessButton["state"] = "normal"
		self.hintLabel["text"] = "Guess a number between 1 and 100"
		self.guessField["value"] = 0
# definition of the main() method which will establish class objects
def main():
	# instantiates an object from the class into mainloop()
	GuessingGame().mainloop()
# global call to the main() method
main()