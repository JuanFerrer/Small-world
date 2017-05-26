import input

class Player:
	def __init__(self):
		self._pos = [0, 0]
		self.knownPos = []
	
	# Set starting position
	def setPos(self, pos):
		self._pos = [pos[0], pos[1]]
	
	# Accessor
	def getPos(self):
		return self._pos
	
	# Move player in the specified direction. Can't move through diagonals
	def move(self, board):
		dir = input.getPlayerMove()
		self.makeMove(dir, board)
		return True

	def posFromDir(self, dir):
		newPos = self._pos
		if dir == "up" and self._pos[0] > 0:
			return [newPos[0] - 1, newPos[1]]
		elif dir == "down" and self._pos[0] < 9:
			return [newPos[0] + 1, newPos[1]]
		elif dir == "right" and self._pos[1] < 9:
			return [newPos[0], newPos[1] + 1]
		elif dir == "left" and self._pos[1] > 0:	
			return [newPos[0], newPos[1] - 1]


	def makeMove(self, dir, board):
		if dir != "":
			if self._pos not in self.knownPos:
				self.knownPos.append(self._pos)
			newPos = self.posFromDir(dir)
			if newPos and newPos[0] >= 0 and newPos[0] < board.getHeight() \
			and newPos[1] >= 0 and newPos[1] < board.getWidth():
				self._pos = newPos
				return True
		return False
		
		# newPos = self._pos
			
		# if dir == "up" and self._pos[0] > 0:
		# 	self._pos = [newPos[0] - 1, newPos[1]]
		# elif dir == "down" and self._pos[0] < 9:
		# 	self._pos = [newPos[0] + 1, newPos[1]]
		# elif dir == "right" and self._pos[1] < 9:
		# 	self._pos = [newPos[0], newPos[1] + 1]
		# elif dir == "left" and self._pos[1] > 0:	
		# 	self._pos = [newPos[0], newPos[1] - 1]