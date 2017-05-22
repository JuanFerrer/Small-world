# http://www.redblobgames.com/pathfinding/a-star/implementation.html
# https://en.wikipedia.org/wiki/A*_search_algorithm
import Queue
import subjectivemap

def aStarSearch(board, start, goal, ):
    closedSet = set()
    openSet = Queue.PriorityQueue()
    openSet.put(start, 0)
    cameFrom = set()
    cameFrom[start] = None
    gScore = set()
    gScore[start] = 0
    fScore = set()
    fScore[start] = board.costBetween(start, goal)

    while not openSet.empty():
        current = openSet.get()

        if current == goal:
            break

        closedSet.add(current)
        
        for neighbour in board.getAdjacentTo(current):
            if neighbour in closedSet:
                pass    # We've seen this already. Just ignore
            newScore = gScore[current] + board.distBetween(current, neighbour)
            if neighbour not in openSet:
                openSet.put(neighbour)
            elif newScore >= gScore[neighbour]:
                pass # Not a better path

            cameFrom[neighbour] = current
            gScore[neighbour] = newScore
            fScore[neighbour] = gScore[neighbour] + board.costBetween(neighbour, goal)

    return getFullPath(cameFrom, current)

def getFullPath(cameFrom, current):
    totalPath = [current]
    while current in cameFrom: # Needs checking
        current = cameFrom[current]
        totalPath.append(current)
    return totalPath