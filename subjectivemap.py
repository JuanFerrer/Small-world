# Defines how the AI perceives the map
# It's passed to the A* algorithm

import map

class Node:
    def __init__(self, parent, score, pos):
        self.parent = parent
        self.score = score
        self.pos = pos
    def __eq__(self, other):
        return self.pos == other.pos 

# Can't go through 0, only through 1
class SubjectiveMap (map.Map):
    def __init__(self, w, h, knownPos):
        self._table = [[0 for x in range(w)] for y in range(h)]
        self._width = w
        self._height = h
        for i in range(self._width):
            for j in range(self._height):
                if [i, j] in knownPos:
                    self._table[i][j] = 1

    def getCostAt(self, i, j):
        return self._table[i][j]
    def getCostAt(self, pos):
        return self._table[pos[0]][pos[1]]

    def costBetween(self, square1, square2):
        map.Map.distBetween(square1, square2)

    # Get a list of visited adjacent squares
    def getAdjacentTo(self, pos):
        # n = [pos[0] - 1, pos[1]] if pos[0] > 0 \
        #     else [pos[0] + 1, pos[1]]  # s
        # e = [pos[0], pos[1] + 1] if pos[1] < self._width - 1 \
        #     else [pos[0], pos[1] - 1]  # w
        # s = [pos[0] + 1, pos[1]] if pos[0] < self._height - 1 else n
        # w = [pos[0], pos[1] - 1] if pos[1] > 0 else e
        dirs = map.Map.getAdjacentTo(self, pos);

        return [Node(None, None, dirs[0]), \
                Node(None, None, dirs[0]), \
                Node(None, None, dirs[0]), \
                Node(None, None, dirs[0])]
