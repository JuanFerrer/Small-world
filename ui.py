import os

# Utilities

def cls():
    os.system('cls')

def suicide():
	print("There's no escape. You shoot yourself...");


def printThreats(pos, map):
	threatsNear = map.checkNear(pos)
	if threatsNear[0]:
		print("A suspicious breeze brushes your hair...")
	if threatsNear[1]:
		print("A stench fills your lungs...")
