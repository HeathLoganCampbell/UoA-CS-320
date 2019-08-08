'''
UPI: HCAM630
NAME: HEATH LOGAN CAMPBELL

THIS PROGRAM FINDS THE SHORTEST PATH IN A GRID
'''
import sys


def isValid(map, pos):
    height = len(map) + 1
    width = len(map[0]) + 1

    return (pos[0] <= width and pos[0] >= 0) and (pos[1] <= height and pos[1] >= 0)


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
            possiblePaths.append((nextPosition, 1))
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

    if(size[0] == size[1] == 0):
        break

    map = []
    for i in range(size[0]):
        predecessor = (sys.stdin.readline().rstrip("\n"))
        if(predecessor == ''):
            break
        row = [int(s) for s in predecessor.split(' ')]
        map.append(row)
    bottomLeftChunk = (0, len(map) + 1)
    dijkstra(map, bottomLeftChunk)
