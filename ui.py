import os

# Utilities

def cls():
    os.system('cls')

def pause():
	os.system("pause")

def suicide():
	print("There's no escape. You shoot yourself...")

def reachedGoal():
	print("Congratulations! You found the exit!")

def printThreats(pos, map):
	threatsNear = map.checkNear(pos)
	if threatsNear[0]:
		print("A suspicious breeze brushes your hair...")
	if threatsNear[1]:
		print("A stench fills your lungs...")
