import space
import player
import input
import ui
import map

import random
w, h = 10, 10
spaces =   [[space.Space() for i in xrange(w)] for j in xrange(h)]
			
goal = [0, 0]
			


monsters = 2
holes = 3

mUsed = 0 # Monsters used
hUsed = 0 # Holes used

for i in xrange(w):
	for j in xrange(h):
		if random.randint(0, 1) == 1: # Using special square			
			makeHole = random.randint(0, 1)
			if makeHole == 1 and hUsed <= holes:
				spaces[i][j] = 1
				hUsed += 1
			elif makeHole == 0 and mUsed <= monsters:
				spaces[i][j] = 2
				mUsed += 1
			else:
				spaces[i][j] = 0
		else:
			spaces[i][j] = 0

goal = [random.randint(0, w - 1), random.randint(0, h - 1)];
spaces[goal[0]][goal[1]] = 4
spaces[random.randint(0, w - 1)][random.randint(0, h - 1)] = 8
			
			

# Setup
board = map.Map(w, h)
p = player.Player()	
		
# Initialisation
board.initialise(spaces)
p.setPos(board.getStart())
	
board.show(p)
# Loop
while p.getPos() != goal:
	key = input.listenKey()
	if key != "":
		ui.cls()
		if key == "esc":
			break
		if key in ["up", "left", "down", "right"]:
			p.move(key)
		key = ""
	board.show(p)
	board.checkNear(p.getPos())
	
	
