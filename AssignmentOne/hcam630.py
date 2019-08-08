'''
UPI: HCAM630
NAME: HEATH LOGAN CAMPBELL

THIS PROGRAM FINDS THE SHORTEST PATH IN A GRID
'''
import sys


def isValid(map, pos):
    height = len(map)
    width = len(map[0])

    return (pos[1] <= width and pos[1] >= 0) and (pos[0] <= height and pos[0] >= 0)


'''
0,0    0,1    0,2

1,0    1,1    1,2

2,0    2,1    2,2

3,0    3,1    2,2
'''


'''
every route has 2 path excluding diangals and edges
'''


def getPaths(map, position):
    positionsArray = []
    possiblePaths = []
    # Up
    positionsArray.append((position[0], position[1] + 1))
    # Up Right
    positionsArray.append((position[0] + 1, position[1] + 1))
    # Right
    positionsArray.append((position[0] + 1, position[1]))
    # Down Right
    positionsArray.append((position[0] + 1, position[1] - 1))
    # Down
    positionsArray.append((position[0], position[1] - 1))
    # Down Left
    positionsArray.append((position[0] - 1, position[1] - 1))
    # Left
    positionsArray.append((position[0] - 1, position[1]))
    # Up Left
    positionsArray.append((position[0] - 1, position[1] + 1))

    for nextPosition in positionsArray:
        if(isValid(map, nextPosition)):
            possiblePaths.append(nextPosition)
    return possiblePaths


'''
We start at the bottom left of the map and have
to find the shortest path to the top right.
Each corner is a node, giving us a maximime of
12 path and a min of 3 in the corners.
'''


def dijkstra(map, position):
    height = len(map) + 1
    width = len(map[0]) + 1
    print(height, width, map)
    # bottom left
    possiblePaths = getPaths(map, position)
    print(possiblePaths)


while(True):
    predecessor = (sys.stdin.readline().rstrip("\n"))
    if(predecessor == ''):
        break
    size = [int(s) for s in predecessor.split(' ')]

    height = size[0]
    width = size[1]
    if(width == height == 0):
        break
    height = height + 1
    width = width + 1

    map = []
    for i in range(size[0]):
        predecessor = (sys.stdin.readline().rstrip("\n"))
        if(predecessor == ''):
            break
        row = [int(s) for s in predecessor.split(' ')]
        map.append(row)
    bottomLeftChunk = (0, len(map) + 1)

    realMap = []
    for i in range(height):
        realMap.append([10000000000] * width)
    startPos = (height - 1, 0)
    visted = [startPos]
    realMap[startPos[0]][startPos[1]] = 0

    # Get all possible next paths
    # We could move up
    realMap[startPos[0] - 1][startPos[1]
                             ] = map[startPos[0] - 1][startPos[1]]
    # We could move up right
    realMap[startPos[0] - 1][startPos[1] +
                             1] = map[startPos[0] - 1][startPos[1] + 1 - 1]
    #  We could move right
    realMap[startPos[0]][startPos[1] +
                         1] = map[startPos[0] - 1][startPos[1] - 1 + 1]

    # round 2
    currentWeight = realMap[startPos[0] - 1][startPos[1]]
    realMap[startPos[0] - 1 - 1][startPos[1]] = currentWeight + map[startPos[0] - 1 - 1][startPos[1]]

    realMap[startPos[0] - 1 - 1][startPos[1] + 1] = currentWeight + map[startPos[0] - 1 - 1][startPos[1]]

    nextPos = currentWeight + map[startPos[0] - 1][startPos[1]+1]
    if(realMap[startPos[0] - 1 - 1][startPos[1] + 1] > nextPos):
      realMap[startPos[0] - 1 - 1][startPos[1] + 1] = map[startPos[0] - 1][startPos[1]+1]

    # round 3
    currentWeight = realMap[startPos[0] - 1][startPos[1] + 1]
    nextPos = currentWeight + map[startPos[0] - 1 - 1][startPos[1] + 1]
    if(realMap[startPos[0] - 1 - 1][startPos[1] + 1] > nextPos):
      realMap[startPos[0] - 1 - 1][startPos[1] + 1] = nextPos

    nextPos = currentWeight + map[startPos[0] - 1 - 1][startPos[1] + 1]
    if(realMap[startPos[0] - 1 - 1][startPos[1] + 1 + 1] > nextPos):
      realMap[startPos[0] - 1 - 1][startPos[1] + 1 + 1] = nextPos
   
      nextPos = currentWeight + map[startPos[0] - 1 - 1][startPos[1] + 1]
    if(realMap[startPos[0] - 1][startPos[1] + 1 + 1] > nextPos):
      realMap[startPos[0] - 1][startPos[1] + 1 + 1] = nextPos
    
    print(realMap)
