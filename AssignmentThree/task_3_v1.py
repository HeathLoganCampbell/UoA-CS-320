# first n is how many lines (n <= 1000)
# 
import sys
import heapq 

def min(a, b):
  if(a < b):
    return a
  return b

def max(a, b):
  if(a > b):
    return a
  return b


def problemThree(span_time):
  rooms = []
  periods = [span_time[0]]
  largestDist = -1
  for x in range(len(span_time)):
    start = span_time[x][0]
    end = span_time[x][1]
    distance = span_time[x][2]

    lastMerge = periods[-1]
    lastEnd = lastMerge[1]
    if(start <= lastEnd):
      lastMerge[1] = max(lastEnd, end)
      newDist = (lastMerge[1] - lastMerge[0])
      if(largestDist < newDist):
        largestDist = newDist
    else:
      periods.append(span_time[x])
      newDist = (span_time[x][1] - span_time[x][0])
      if(largestDist < newDist):
        largestDist = newDist
  print(largestDist)


def getKey(elem):
    return elem[0]

predecessor = (sys.stdin.readline().rstrip("\n"))
test_cases = int(predecessor)

while(True):
    predecessor = (sys.stdin.readline().rstrip("\n"))
    # if line is blank, we leave
    if(predecessor == ''):
        break
    if(test_cases == 0):
        break
    cord_pair = list(map(int, predecessor.split()))
    span_time = []
    for x in range(len(cord_pair) // 2):
      start = (cord_pair[(x*2)])
      end = (cord_pair[(x*2)+1])
      distance = end - start
      span_time.append([start, end, distance])
    span_time = sorted(span_time, key = getKey)
    problemThree(span_time)
    test_cases -= 1

