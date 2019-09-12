import sys

def distX(a, b):
  return a[0] - b[0]

def distY(a, b):
  return a[1] - b[1]

def dist(a, b):
  return distX(a, b) * distX(a, b) + distY(a, b) * distY(a, b) 

def bruteForce(points):
  smallest_dist = 1000000000000
  for i in range(len(points)):
    for j in range( (i + 1),len(points)):
      current_distance = dist(points[i], points[j])
      if(smallest_dist > current_distance):
        smallest_dist = current_distance
  return smallest_dist

points = []

while(True):
    predecessor = (sys.stdin.readline().rstrip("\n"))
    # if line is blank, we leave
    if(predecessor == ''):
        break
    cord_pair = list(map(int, predecessor.split()))
    points.append(cord_pair)

print(bruteForce(points))