#
#	O O O O O O O O O O
#	O O O O O O O O O O
#	O O O O O O O O O O
#	O O O O O O O O O O
#	O O O O O O O O O O
#	O O O O O O O O O O
#	O O O O O O O O O O
#	O O O O O O O O O O
#	O O O O O O O O O O
#

# Used to set bool flags
# The 4 flags are (RTL):
# 	1 - has hole
#	2 - has monster
#	3 - has gold
#   4 - is start
def binary(num, length = 4):
    binary_string_list = list(format(num, '0{}b'.format(length)))
    return [int(digit) for digit in binary_string_list]

# Action of a space
# class Action:
	# def __init__(self):
		# _isOnEnter = true
		# _isOnExit = false
		
	# def execute():
		# pass
	
	# def isOnEnter():
		# return _isOnEnter
		
	# def isOnExit():
		# return _isOnExit
		
		
		
# Each of the grid spaces
class Space:
	def __init__(self):
		self.initialise(0)
		
	def initialise(self, type):
		flags = binary(type, 4)
		self._isStart = flags[0]
		self._hasGold = flags[1]
		self._hasMonster = flags[2]
		self._hasHole = flags[3]
		#checkNear()
	
	def isStart(self):
		return self._isStart == 1
	
	def hasGold(self):
		return self._hasGold == 1
		
	def hasMonster(self):
		return self._hasMonster == 1
		
	def hasHole(self):
		return self._hasHole == 1
		
	def getImage(self):
		if self.hasMonster():
			return "M"
		elif self.hasHole():
			return "O"
		elif self.hasGold():
			return "#"
		else:
			return " "
	# def enter(self):
	# 	for action in actions:
	# 		if action.isOnEnter():
	# 			action.execute()
		
	# def exit(self):
	# 	for action in actions:
	# 		if action.isOnExit():
	# 			action.execute()
	