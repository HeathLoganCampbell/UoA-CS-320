'''
UPI: HCAM630
NAME: HEATH LOGAN CAMPBELL

THIS PROGRAM FINDS THE SHORTEST PATH IN A GRID
'''
import heapq
import sys


while(True):
    predecessor = (sys.stdin.readline().rstrip("\n"))
    if(predecessor == ''):
        break
    size = [int(s) for s in predecessor.split(' ') if s != '']

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
        row = [int(s) for s in predecessor.split(' ') if s != '']
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

    seen = []
    
    currentPos = startPos
    while(True):
      for pos in [(-1,0,0,1), (-1, 1, 0, 1), (0, 1, 0, 1),   (1, 1, 0, 1), (1, 0, 0, 1), (1, -1, 0, 1), (0, -1, 0, 1), (-1, -1, 0, 1)]:
        vertY = currentPos[0] + pos[0]
        vertX = currentPos[1] + pos[1]
        if(vertY < 0 or vertY >= len(realMap)):
          continue
        if(vertX < 0 or vertX >= len(realMap[0])):
          continue
        vertixLoc = realMap[vertY][vertX]

        weightY = currentPos[0] + pos[2] - 1
        weightX = currentPos[1] + pos[3] - 1
        if(weightY < 0 or weightY >= len(map)):
          continue
        if(weightX < 0 or weightX >= len(map[0])):
          continue
        
        if(currentPos[0] < 0 or currentPos[0] >= len(realMap)):
          continue
        if(currentPos[1] < 0 or currentPos[1] >= len(realMap[0])):
          continue
        

        weights = realMap[currentPos[0]][currentPos[1]] + map[weightY][weightX]
        if(vertixLoc > weights):
          realMap[currentPos[0] + pos[0]][currentPos[1] + pos[1]] = weights
          seen.append((currentPos[0] + pos[0], currentPos[1] + pos[1], weights))
          # Might be wrong?
          if(currentPos[0] + pos[0] == 0 and currentPos[1] + pos[1] == width - 1 ):
            break
      seen.sort(key=lambda tup: tup[2])
      # print(seen)
      currentPos = seen.pop(0)
      if(len(seen) == 0):
        break

    # print(realMap)
    print(realMap[0][width - 1])
