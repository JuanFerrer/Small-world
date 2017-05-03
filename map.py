from __future__ import print_function
import space

class Map:
	def __init__(self, w, h):
		self._table = [[space.Space() for x in xrange(w)] for y in xrange(h)]
		self._width = w
		self._height = h
		
	def initialise(self, lists):
		for i in xrange(self._width):
			for j in xrange(self._height):
				self._table[i][j].initialise(lists[i][j])
		
		
	def show(self, p):
		for i in xrange(self._width):
			for j in xrange(self._height):
				if p.getPos() == [i, j]:
					print('X', " ", end = "")
				else:
					print(self._table[i][j].getImage() if [i, j] in p.knownPos else '-', " ", end="")
			print()
		
		for pos in p.knownPos:
			print(pos)