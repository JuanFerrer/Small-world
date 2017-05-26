import player
import time
import astar
import subjectivemap

class AIPlayer(player.Player):
    def __init__(self):
        self._pos = [0, 0]
        self.knownPos = []
        self.notThreat = []
        self.maybeHole = []
        self.maybeMonster = []
        self.nextMoves = []

    def move(self, board):
        time.sleep(0.1)
        # We'll first look for a good movement
        dir = self.findBestMove(board)
        # Then call the base class method to act
        #self.makeMove()
        return self.makeMove(dir)

    def findBestMove(self, board):
        #   Algorithm:
        #
        #   1 Update threat lists
        #
        #   2 Move to closest square that is definitely not a threat
        #
        self.updateThreats(board)
        dir = ""
        # Do we have moves planned?
        if self.nextMoves:
            dir = self.dirFromPos(self.nextMoves.pop(0), self.getPos())

        else:
            for pos in self.notThreat:
                if board.areAdjacent(pos, self.getPos()):
                    dir = self.dirFromPos(pos, self.getPos())
                    break

            if dir == "":
                closestSafeSquare = self.findClosestSafe(board)
                dir = self.dirFromPos(closestSafeSquare, self.getPos()) # Search for the closest safe square
                if self.isDangerousDir(dir): # Make sure you're not stepping over a dangerous square
                    # Need to find a way around the obstacle.
                    # Since we already know which safe square is the closest to us, it's probably
                    # best to implement best-first search algorithm to find quickest path through all known positions
                    self.nextMoves = astar.bestFirstSearch(subjectivemap.SubjectiveMap(board.getWidth(), board.getHeight(), self.knownPos),
                        self.getPos(), closestSafeSquare)
                    if self.nextMoves:                   
                        del self.nextMoves[0]  # Deleting origin
                        dir = self.dirFromPos(self.nextMoves.pop(0), self.getPos())
            # Don't know where to go :(
            if dir == "":
                # dir == "right" # Then choose the right
                # Probably wrong, needs fixing
                pass

        return dir
    
    def isDangerousDir(self, dir):
        newPos = self.posFromDir(dir)
        return newPos in self.maybeHole or newPos in self.maybeMonster


        # Look for closest non-threat square
    def findClosestSafe(self, board):
        closestDist = 100
        closestSafeSquare = []
        for square in self.notThreat:
            newDist = board.distBetween(square, self.getPos())
            if  newDist < closestDist:
                closestDist = newDist
                closestSafeSquare = square
        return closestSafeSquare

    def dirFromPos(self, toPos, fromPos):
        if toPos[0] != fromPos[0]:
            return "up" if toPos[0] < fromPos[0] else "down"
        elif toPos[1] != fromPos[1]:
            return "left" if toPos[1] < fromPos[1] else "right"

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
                    if square not in self.notThreat and square not in self.knownPos:
                        self.notThreat.append(square)
        # Make sure I don't visit again the positions I know
        for pos in self.knownPos:
            if pos in self.notThreat:
                self.notThreat.remove(pos)
