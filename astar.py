# http://www.redblobgames.com/pathfinding/a-star/implementation.html
# https://en.wikipedia.org/wiki/A*_search_algorithm
# https://gist.github.com/jamiees2/5531924

class Node:
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos
        self.parent = None
        self.G = 0 # Cost of the path from Start to here
        self.H = 0 # Heuristic from here to Goal
    def moveCost(self):
        return 0 if self.value == "." else 1

import subjectivemap

def aStarSearch(board, start, goal):
    closedSet = set()
    openSet = set()
    current = start
    openSet.add(current)
    while openset:
        current = min(openSet, key=lambda o:o.G + o.H)

        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]

    openSet.remove(current)
    closedSet.add(current)
    for node in board.getAdjacentTo(current):
        if node in closedSet:
            continue
        if node in openSet:
            newG = current.G + current.moveCost(node)
            if node.G > newG:
                node.G = newG
                node.parent = current
        else:
            node.G = current.G + current.moveCost(node)
            node.H = board.distBetween(node, goal)
            node.parent = current
            openSet.add(node)

    return []