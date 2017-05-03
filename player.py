

class Player:
	def __init__(self):
		self._pos = [0, 0]
		
	def getPos(self):
		return self._pos
	
	def move(self, dir):
		if dir == 2:
			self._pos[1] += 1