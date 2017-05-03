import space
import player
import input
import ui
import map

spaces =   [[0, 0, 0, 0, 0],
			[0, 1, 0, 0, 0],
			[0, 0, 4, 2, 1],
			[0, 2, 1, 0, 0],
			[8, 0, 0, 0, 0]]

w, h = 5, 5

# Setup
board = map.Map(w, h)
p = player.Player()	
		
# Initialisation
board.initialise(spaces)
	
board.show(p)
# Loop
while p.getPos() != [2, 2]:
	key = input.listenKey()
	if key != "":
		ui.cls()
		if key == "esc":
			break
		if key in ["up", "left", "down", "right"]:
			p.move(key)
		key = ""
	board.show(p)
	
	
