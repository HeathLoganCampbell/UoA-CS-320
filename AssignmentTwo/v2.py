from math import sqrt, pow
import sys
from datetime import datetime 

def distance(a, b):
  return pow(a[0] - b[0],2) + pow(a[1] - b[1],2)



def bruteMin(points, current=float("inf")):
  if len(points) < 2: return current
  else:
    head = points[0]
    del points[0]
    newMin = min([distance(head, x) for x in points])
    newCurrent = min([newMin, current])
    return bruteMin(points, newCurrent)

def divideMin(points):
  half = len(sorted(points))//2
  minimum = min([bruteMin(points[:half]), bruteMin(points[half:])])
  nearLine = filter(lambda x: x[0] > half - minimum and x[0] < half + minimum, points)
  return min([bruteMin(nearLine), minimum])


points = []

while(True):
    predecessor = (sys.stdin.readline().rstrip("\n"))
    # if line is blank, we leave
    if(predecessor == ''):
        break
    cordPair = list(map(int, predecessor.split()))
    points.append(cordPair)
    

start_time = datetime.now() 

print(divideMin(points))

time_elapsed = datetime.now() - start_time 
print('Time elapsed (ms) {}'.format(time_elapsed))
