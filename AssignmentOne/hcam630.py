'''
UPI: HCAM630
NAME: HEATH LOGAN CAMPBELL

THIS PROGRAM FINDS THE SHORTEST PATH IN A GRID
'''
import heapq
import sys

while(True):
    predecessor = (sys.stdin.readline().rstrip("\n"))
    # if line is blank, we leave
    if(predecessor == ''):
        break
    size = [int(s) for s in predecessor.split(' ') if s != '']

    height = size[0]
    width = size[1]
    # if size is nothing, we leave
    if(width == height == 0):
        break
    # We will have n + 1 nodes where n is tiles
    # because we always have an extra node
    height = height + 1
    width = width + 1

    # map of tile weights
    map = []
    for i in range(size[0]):
        predecessor = (sys.stdin.readline().rstrip("\n"))
        if(predecessor == ''):
            break
        row = [int(s) for s in predecessor.split(' ') if s != '']
        map.append(row)
    bottomLeftChunk = (0, len(map) + 1)

    # Set all values to basically infinity
    # map of nodes, with the distances to get to them
    realMap = []
    for i in range(height):
        realMap.append([10000000000] * width)
    # Format of edge is (Weight, Y, X), this is so we don't 
    # have to modify heap, as it'll use the first element
    startPos = (0,height - 1, 0)
    visted = [startPos]
    realMap[startPos[1]][startPos[2]] = startPos[0]

    # List of next paths
    seen = []
    # Use a heap to miminize shorting
    heapq.heapify(seen) 

    currentPos = startPos
    while(True):
      # all possible ways we can go
      for pos in [(-1,0,0,1), (-1, 1, 0, 1), (0, 1, 0, 1),   (1, 1, 0, 1), (1, 0, 0, 1), (1, -1, 0, 1), (0, -1, 0, 1), (-1, -1, 0, 1)]:
        vertY = currentPos[1] + pos[0]
        vertX = currentPos[2] + pos[1]
        if(vertY < 0 or vertY >= len(realMap)):
          continue
        if(vertX < 0 or vertX >= len(realMap[0])):
          continue
        vertixLoc = realMap[vertY][vertX]

        weightY = currentPos[1] + pos[2] - 1
        weightX = currentPos[2] + pos[3] - 1
        if(weightY < 0 or weightY >= len(map)):
          continue
        if(weightX < 0 or weightX >= len(map[0])):
          continue
        
        if(currentPos[1] < 0 or currentPos[1] >= len(realMap)):
          continue
        if(currentPos[2] < 0 or currentPos[2] >= len(realMap[0])):
          continue
        

        weights = realMap[currentPos[1]][currentPos[2]] + map[weightY][weightX]
        if(vertixLoc > weights):
          realMap[currentPos[1] + pos[0]][currentPos[2] + pos[1]] = weights
          heapq.heappush(seen, (weights, currentPos[1] + pos[0], currentPos[2] + pos[1])) 
          # If we made it to the top left, just end the program and print the answer
          if(currentPos[1] + pos[0] == 0 and currentPos[2] + pos[1] == width - 1 ):
            break
     
      # print(seen)
      currentPos = heapq.heappop(seen)
      if(len(seen) == 0):
        break

    # print(realMap)
    print(realMap[0][width - 1])
