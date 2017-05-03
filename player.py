class Player:
	def __init__(self):
		self._pos = [0, 0]
		self.knownPos = []
	
	def setPos(self, board):
		for i in xrange(board.getWidth()):
			for j in xrange(board.getHeight()):
				if board.getAt(i, j).isStart():
					self._pos = [i, j]
					return
	
	def getPos(self):
		return self._pos
	
	def move(self, dir):
		if self._pos not in self.knownPos:
			self.knownPos.append(self._pos)
		
		newPos = self._pos
			
		if dir == "up" and self._pos[0] > 0:
			self._pos = [newPos[0] - 1, newPos[1]]
		elif dir == "down" and self._pos[0] < 4:
			self._pos = [newPos[0] + 1, newPos[1]]
		elif dir == "right" and self._pos[1] < 4:
			self._pos = [newPos[0], newPos[1] + 1]
		elif dir == "left" and self._pos[1] > 0:	
			self._pos = [newPos[0], newPos[1] - 1]