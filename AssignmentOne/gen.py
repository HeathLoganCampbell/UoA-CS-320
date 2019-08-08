import random

height = 400
width = 400

for y in range(height):
  line = []
  for x in range(width):
    line.append(str(random.randint(1,101)))
  print(' '.join(line))