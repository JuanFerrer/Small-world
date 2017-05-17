from __future__ import print_function
import space

class Map:
	def __init__(self, w, h):
		self._table = [[space.Space() for x in range(w)] for y in range(h)]
		self._width = w
		self._height = h
	
	# Find the width of the board
	def getWidth(self):
		return self._width
	
	# Find the height of the board
	def getHeight(self):
		return self._height
	
	# Initialise each space
	def initialise(self, lists):
		for i in range(self._width):
			for j in range(self._height):
				self._table[i][j].initialise(lists[i][j])
	
	# Accessor
	def getAt(self, row, col):
		return self._table[row][col]
		
	def getAt(self, pos):
		return self._table[pos[0]][pos[1]]
		
	# Get the starting position
	def getStart(self):
		for i in range(self._width):
			for j in range(self._height):
				if self._table[i][j].isStart():
					return [i, j]
	
	# Print board
	def show(self, p):
		for i in range(self._width):
			for j in range(self._height):
				if p.getPos() == [i, j]:
					print('X', ' ', end = '')
				else:
					print(self._table[i][j].getImage() if [i, j] in p.knownPos else '-', ' ', end='')
			print()

	# Get a list with all adjacent squares. Diagonals don't count as adjacent
	def getAdjacentTo(self, pos):
		n = [pos[0] - 1, pos[1]] if pos[0] > 0 else [pos[0] - 1, pos[1]] #s
		e = [pos[0], pos[1] + 1] if pos[1] < self._width - 1 else [pos[0], pos[1] - 1] #w
		s = [pos[0] + 1, pos[1]] if pos[0] < self._height - 1 else n
		w = [pos[0], pos[1] - 1] if pos[1] > 0 else e

		return [n, e, s, w]

	
	# Check squares around the player and print messages when appropriate
	#
	#	[ N/A  ] [-1, 0 ] [  N/A ]
	#	[ 0,-1 ] [ 0, 0 ] [ 0, 1 ]
	#	[ N/A  ] [ 1, 0 ] [  N/A ]
	def checkNear(self, pos):
		adjacentSquares = self.getAdjacentTo(pos)
	
		if any(self.getAt(dir).hasMonster() for dir in adjacentSquares):
			print("A stench fills your lungs...")
			
		if any(self.getAt(dir).hasHole() for dir in adjacentSquares):
		 	print("A suspicious breeze brushes your hair...")
