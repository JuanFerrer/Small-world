import player

class AIPlayer(player.Player):
    def __init__(self):
        self._pos = [0, 0]
		self.knownPos = []
        self.maybeHole = []
        self.maybeMonster = []
    def move(self):
        # We'll first look for a good movement
        self.findBestMove()
        # Then call the base class method to act
        Player.move(self, dir)

    def findBestMove(self, map):
        pass
        #   Algorithm: On getting to new position
        #   
        #   1 Update threat lists
        # 
        #   2 Move to square that is definitely not a threat
        # 
        #   3 If none, move back and repeat 
        #   
        #


    def areSharingAdjacentSquare(self, square1, square2, shared, map):
        adjacentTo1 = map.getAdjacentTo(square1)
        adjacentTo2 = map.getAdjacentTo(square2)

        if shared in adjacentTo1 and shared in adjacentTo2:
            return True
