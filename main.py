import player
import ai
import ui
import map

import random
w, h = 10, 10
spaces = [[0 for i in range(w)] for j in range(h)]

holes = int(w / 2)
monsters = int(w / 3)

for i in range(holes):  # Spawn holes
    spaces[random.randint(1, w - 2)][random.randint(1, h - 2)] = 1
for i in range(monsters):  # Spawn monsters
    spaces[random.randint(1, w - 2)][random.randint(1, h - 2)] = 2
goal = [random.randint(0, w - 1), random.randint(0, h - 1)]
spaces[goal[0]][goal[1]] = 4
# Or should it be [0, 0]?
start = [random.randint(0, w - 1), random.randint(0, h - 1)]
spaces[start[0]][start[1]] = 8

# Setup
board = map.Map(w, h)
p = ai.AIPlayer()
#p = player.Player()

# Initialisation
board.initialise(spaces)
p.setPos(board.getStart())

board.show(p)

# Loop
while p.getPos() != goal:
    p.move(board)
    ui.cls()
    board.show(p)
    ui.printThreats(p.getPos(), board)
