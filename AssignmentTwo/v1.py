'''
UPI: HCAM630
NAME: HEATH LOGAN CAMPBELL

'''
import sys
from functools import cmp_to_key
from datetime import datetime 


def distX(a, b):
  return a[0] - b[0]

def distY(a, b):
  return a[1] - b[1]

def dist(a, b):
  return distX(a, b) * distX(a, b) + distY(a, b) * distY(a, b) 

'''
takes a min point
'''
def min(a, b):
  if (a < b):
    return a
  return b

'''
Brute forces all the points to find the closest
'''
def brute(points):
    minDist = dist(points[0], points[1])
    pointsCount = len(points)
    if pointsCount == 2:
        return minDist
    for i in range(pointsCount-1):
        for j in range(i + 1, pointsCount):
            if i != 0 and j != 1:
              continue
            curDist = dist(points[i], points[j])
            if curDist < minDist:  
                minDist = curDist
    return minDist

def bruteForce(points):
    min = sys.maxsize

    for i in range(len(points)):
      for j in range(i+1, len(points)):
            if (dist(points[i], points[j]) < min):
                min = dist(points[i], points[j]);  
    
    return min

def stripClosest(listX, listY, minDist):  
    pointXCount = len(listX)
    pointXX = listX[pointXCount // 2][0]
    listOfYs = [x for x in listY if pointXX - minDist <= x[0] <= pointXX + minDist]
    best = minDist 
    pointYCount = len(listOfYs)
    for i in range(pointYCount - 1):
        for j in range(i + 1, min(i + 7, pointYCount)):
            dst = dist(listOfYs[i], listOfYs[j])
            if dst < best:
                best = dst
    return best

def closestUtil(sortedByX, ay):
    rangeDiff = len(sortedByX)
    if(rangeDiff <= 3):  
        return bruteForce(sortedByX)
    mid = (rangeDiff) // 2;  
    
    leftX = sortedByX[:mid]
    rightX = sortedByX[mid:]

    midpoint = sortedByX[mid][0]

    leftY = list()
    rightY = list()
    for x in ay:
        if x[0] <= midpoint:
          leftY.append(x)
        else:
          rightY.append(x)
  
    out1 = closestUtil(leftX, leftY)
    out2 = closestUtil(rightX, rightY)

    if out1 <= out2:
        minDist = out1
    else:
        minDist = out2

    stripDist = stripClosest(sortedByX, ay, minDist)
    if minDist <= stripDist:
        return minDist
    else:
        return stripDist

points = []

while(True):
    predecessor = (sys.stdin.readline().rstrip("\n"))
    # if line is blank, we leave
    if(predecessor == ''):
        break
    cordPair = list(map(int, predecessor.split()))
    points.append(cordPair)
    

start_time = datetime.now() 
# Takes about 1.2 second to sort
sortedByX = sorted(points, key=lambda x: x[0])
sortedByY = sorted(points, key=lambda x: x[1])
time_elapsed = datetime.now() - start_time 
print('Time elapsed (ms) {}'.format(time_elapsed))
print("sorted")
print(closestUtil(sortedByX, sortedByY))
