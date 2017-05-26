# http://www.redblobgames.com/pathfinding/a-star/implementation.html
# https://en.wikipedia.org/wiki/A*_search_algorithm
# https://gist.github.com/jamiees2/5531924

import subjectivemap
from subjectivemap import Node

def bestFirstSearch(board, startPos, goalPos):
    # Create openList and closedList
    openList = []
    closedList = []

    # Initialise start and push to openList
    start = Node(None, board.distBetween(startPos, goalPos), startPos)
    openList.append(start)

    # Until goal is found
    while openList:
        current = openList[0]
        openList.remove(current)
        
        if current.pos == goalPos:
            return constructPath(current)
        
        for node in board.getAdjacentTo(current.pos):
            node.score = board.distBetween(node.pos, goalPos)

            if node.pos == goalPos or node not in closedList and node not in openList and board.getCostAt(node.pos) > 0:
                node.parent = current
                openList.append(node)
        
        closedList.append(current)

    return []   # Fail, no path found

# Build path and return
def constructPath(current):
    path = []
    while current:
        path.append(current.pos)
        current = current.parent
    path.reverse()
    return path
