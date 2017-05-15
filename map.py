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
	
	# Check squares around the player and print messages when appropriate
	#
	#	[-1,-1 ] [-1, 0 ] [-1, 1 ]
	#	[ 0,-1 ] [ 0, 0 ] [ 0, 1 ]
	#	[ 1,-1 ] [ 1, 0 ] [ 1, 1 ]
	def checkNear(self, pos):
		n = [pos[0] - 1, pos[1]] if pos[0] > 0 else [pos[0] - 1, pos[1]] #s
		e = [pos[0], pos[1] + 1] if pos[1] < self._width - 1 else [pos[0], pos[1] - 1] #w
		s = [pos[0] + 1, pos[1]] if pos[0] < self._height - 1 else n
		w = [pos[0], pos[1] - 1] if pos[1] > 0 else e
	
		if self.getAt(n).hasMonster() or \
		   self.getAt(e).hasMonster() or \
		   self.getAt(s).hasMonster() or \
		   self.getAt(w).hasMonster():
			print("A stench fills your lungs...")
			
		if self.getAt(n).hasHole() or \
		   self.getAt(e).hasHole() or \
		   self.getAt(s).hasHole() or \
		   self.getAt(w).hasHole():
			print("A suspicious breeze brushes your hair...")