from __future__ import print_function
import space

lSpaces =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
			
spaces =   [[0, 0, 0, 0, 0],
			[0, 1, 0, 0, 0],
			[0, 0, 4, 2, 1],
			[0, 2, 1, 0, 0],
			[8, 0, 0, 0, 0]]

w, h = 5, 5

# Create map
map = [[space.Space() for x in xrange(w)] for y in xrange(h)]

# Initialise spaces
for i in xrange(w):
	print()
	for j in xrange(h):
		#print(map[i][j].hasHole())
		map[i][j].initialise(spaces[i][j])
		print(2 if map[i][j].hasMonster() else 1 if map[i][j].hasHole() else 0, " ", end = "")
		
while player.:
	
