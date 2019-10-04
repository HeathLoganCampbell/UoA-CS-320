# first n is how many lines (n <= 1000)
# 
import sys

def max(a, b):
  if(a > b):
    return a
  return b

def min(a, b):
  if(a < b):
    return a
  return b

while(True):
    predecessor = (sys.stdin.readline().rstrip("\n"))
    if(predecessor == ''):
        break
    cord_pair = list(map(int, predecessor.split()))
    n = len(cord_pair);
    childOne = 0
    childTwo = 0
    
    # (index, value)
    selectedIndexes = set()
    orderedIndex = [i for i in sorted(enumerate(cord_pair), key=lambda x:x[1], reverse = True)]

    for index in range(n):
      if((len(selectedIndexes) == 0 )
        or (((((orderedIndex[index][0] + 1) % n) not in selectedIndexes) 
        and (((orderedIndex[index][0] - 1) % n)) not in selectedIndexes))):
        childOne += orderedIndex[index][1];
        selectedIndexes.add(orderedIndex[index][0])
      else:
        childTwo += orderedIndex[index][1];
    print(str(childOne) + " " + str(childTwo))

# Make a obj (index, value)
# 