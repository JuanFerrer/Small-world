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
                    print('X', ' ', end='')
                else:
                    print(self._table[i][j].getImage() if [
                          i, j] in p.knownPos else '-', ' ', end='')
            print()

    # Get a list with all adjacent squares. Diagonals don't count as adjacent
    def getAdjacentTo(self, pos):
        n = [pos[0] - 1, pos[1]] if pos[0] > 0 \
            else [pos[0] + 1, pos[1]]  # s
        e = [pos[0], pos[1] + 1] if pos[1] < self._width - 1 \
            else [pos[0], pos[1] - 1]  # w
        s = [pos[0] + 1, pos[1]] if pos[0] < self._height - 1 else n
        w = [pos[0], pos[1] - 1] if pos[1] > 0 else e

        return [n, e, s, w]

    def distBetween(self, square1, square2):
        return abs(square1[0] - square2[0]) + abs(square1[1] - square2[1])

    # Check squares around the player and print messages when appropriate
    #
    #	[ N/A  ] [-1, 0 ] [  N/A ]
    #	[ 0,-1 ] [ 0, 0 ] [ 0, 1 ]
    #	[ N/A  ] [ 1, 0 ] [  N/A ]
    def checkNear(self, pos):
        adjacentSquares = self.getAdjacentTo(pos)
        threats = [False, False]

        if any(self.getAt(dir).hasHole() for dir in adjacentSquares):
            threats[0] = True

        if any(self.getAt(dir).hasMonster() for dir in adjacentSquares):
            threats[1] = True
        return threats

    def areAdjacent(self, square1, square2):
        adjacentTo1 = self.getAdjacentTo(square1)
        return square2 in adjacentTo1

    def areSharingAdjacentSquare(self, square1, square2, shared):
        adjacentTo1 = self.getAdjacentTo(square1)
        adjacentTo2 = self.getAdjacentTo(square2)

        return shared in adjacentTo1 and shared in adjacentTo2
