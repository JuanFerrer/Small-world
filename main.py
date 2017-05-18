import space
import player
import input
import ui
import map

import random
w, h = 10, 10
spaces = [[0 for i in range(w)] for j in range(h)]

monsters = int(w / 3)
holes = int(w / 2)

for i in range(holes):		#Spawn holes
	spaces[random.randint(1, w - 2)][random.randint(1, h - 2)] = 1
for i in range(monsters):	# Spawn monsters
	spaces[random.randint(1, w - 2)][random.randint(1, h - 2)] = 2
goal = [random.randint(0, w - 1), random.randint(0, h - 1)]
spaces[goal[0]][goal[1]] = 4
start = [random.randint(0, w - 1), random.randint(0, h - 1)] # Or should it be [0, 0]?
spaces[start[0]][start[1]] = 8			

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
		if key == "esc":
			break
		if key in ["up", "left", "down", "right"]:
			ui.cls()
			p.move(key)
			board.show(p)
			board.checkNear(p.getPos())
		if key == "enter":
			pass
	key = ""
	