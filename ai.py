import player
import time

class AIPlayer(player.Player):
    def __init__(self):
        self._pos = [0, 0]
        self.knownPos = []
        self.notThreat = []
        self.maybeHole = []
        self.maybeMonster = []

    def move(self, board):
        time.sleep(2)
        # We'll first look for a good movement
        dir = self.findBestMove(board)
        # Then call the base class method to act
        player.Player.makeMove(self, dir)

    def findBestMove(self, board):
        #   Algorithm:
        #
        #   1 Update threat lists
        #
        #   2 Move to square that is definitely not a threat
        #
        #   3 If none, move back and repeat
        #
        #
        self.updateThreats(board)

    def updateThreats(self, board):
        adjacents = board.getAdjacentTo(self.getPos())
        threats = board.checkNear(self.getPos())
        for square in adjacents:
            if square not in self.knownPos:
                if threats[0] and square not in self.maybeHole:
                    self.maybeHole.append(square)
                if threats[1] and square not in self.maybeMonster:
                    self.maybeMonster.append(square)
                if not threats[0] and not threats[1]:
                    if square in self.maybeHole:                 
                        self.maybeHole.remove(square)
                    if square in self.maybeMonster: 
                        self.maybeMonster.remove(square)
                    if square not in self.notThreat:
                        self.notThreat.append(square)



    def areSharingAdjacentSquare(self, square1, square2, shared, board):
        adjacentTo1 = board.getAdjacentTo(square1)
        adjacentTo2 = board.getAdjacentTo(square2)

        if shared in adjacentTo1 and shared in adjacentTo2:
            return True
