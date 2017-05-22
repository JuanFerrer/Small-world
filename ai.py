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
        time.sleep(1)
        # We'll first look for a good movement
        dir = self.findBestMove(board)
        # Then call the base class method to act
        player.Player.makeMove(self, dir)

    def findBestMove(self, board):
        #   Algorithm:
        #
        #   1 Update threat lists
        #
        #   2 Move to closest square that is definitely not a threat
        #
        #
        #
        #
        self.updateThreats(board)
        dir = ""
        for pos in self.notThreat:
            if board.areAdjacent(pos, self.getPos()):
                dir = self.dirFromPos(pos, self.getPos())
                break

        if dir == "":
            dir = self.dirFromPos(self.knownPos[-1], self.getPos()) # Go back if you don't know where to go next

        # Look for closest non-threat square
        closestDist = 100
        closestSquare = []
        for square in self.notThreat:
            newDist = board.distBetween(square, self.getPos())
            if  newDist < closestDist:
                closestDist = newDist
                closestSquare = square
        
        print(closestSquare)

        return dir

    def dirFromPos(self, newPos, currPos):
        if newPos[0] != currPos[0]:
            return "up" if newPos[0] < currPos[0] else "down"
        elif newPos[1] != currPos[1]:
            return "left" if newPos[1] < currPos[1] else "right"

    def updateThreats(self, board):
        if self.getPos() not in self.knownPos:
            self.knownPos.append(self.getPos())
        adjacents = board.getAdjacentTo(self.getPos())
        threats = board.checkNear(self.getPos())
        # Check squares around
        for square in adjacents:
            if square not in self.knownPos and square not in self.notThreat:
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
        # Make sure I don't visit again the positions I know
        for pos in self.knownPos:
            if pos in self.notThreat:
                self.notThreat.remove(pos)
