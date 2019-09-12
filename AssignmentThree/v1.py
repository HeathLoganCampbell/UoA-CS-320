# first n is how many lines (n <= 1000)
# 
import sys

def problemOne(span_time):
  currentDist = 100000
  currentStart = 10000000
  currentEnd = 10000000
  period = []
  queued = False
  for x in range(len(span_time)):
    start = span_time[x][0]
    end = span_time[x][1]
    dist = span_time[x][2]
    if(currentStart < start and queued):
      period.append((currentStart, currentEnd))
      currentStart = currentEnd
      currentEnd = 100000000
      queued = False

    if(start <= currentStart and end <= currentEnd):
      currentStart = start
      currentEnd = end
      queued = True
  if(queued):
    period.append((currentStart, currentEnd))
  print((period))
  


def getKey(elem):
    return elem[1]

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
      span_time.append((start, end, distance))
    span_time = sorted(span_time, key = getKey)
    problemOne(span_time)
    test_cases -= 1

