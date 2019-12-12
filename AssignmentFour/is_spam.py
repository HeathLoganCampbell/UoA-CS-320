import random
import sys
 
# FETCHED PRIME FROM https://primes.utm.edu/lists/small/100000.txt
 
testSize = 1000

totalIteration = 10
totalFalsePositives = 0
for iteration in range(totalIteration):
  emailSize = 1000000
  size = 8000000
  p = 15485863
  a = random.randint(0, p)
  b = random.randint(0, p)
  print("====== #" + str(iteration) + " iteration ======")
  print("a: " + str(a))
  print("b: " + str(b))
  print("prime: " + str(p))
  def hash(email, a, b, p):
      return ((a * email + b) % p) % size
  
  # bitArray = ''.join(['0' for num in range(size)])
  bitArray = [0] * size
  
  # print(''.join(["inserting ", str(emailSize), "..."]))
  # bitArray = [(bitArray[:hIndex] + "1" + bitArray[hIndex+1:]) for i in range(emailSize)]
  for i in range(emailSize):
      hIndex = hash(i, a, b, p)
      bitArray[hIndex] = 1
      # bitArray = bitArray[:hIndex] + "1" + bitArray[hIndex+1:]
  # print("inserted.")
  
  # counts number of 1's in our arrays
  # print("C/ounting 1's...")
  count = str(bitArray).count("1")
  print('There is ' + str(count) + '/' + str(len(bitArray)))
  # Question 1, Probability that a rouge email gets through
  # print("Checking can all whitelisted emails get through...")
  passThroughs = 0
  for i in range(emailSize):
    hIndex = hash(i, a, b, p)
    if(bitArray[hIndex] == 1):
      passThroughs = passThroughs + 1
  print(str(passThroughs) + "/" + str(emailSize) + " whitelisted examils go through")
  
  
  # Question 2, Probability that a rouge email gets through
  # print("Rouge email gets through...")
  flasePassThroughs = 0
  for i in range(0, testSize):
    index = random.randint(emailSize, sys.maxint)
    hIndex = hash(index, a, b, p)
    if(bitArray[hIndex] == 1):
      flasePassThroughs = flasePassThroughs + 1
  totalFalsePositives = totalFalsePositives + flasePassThroughs
  print(str(flasePassThroughs) + "/" + str(testSize) + " not whitelisted emails got through")
  # print(bitArray)
print("=-=-=-=-=-=-=-=-=-")
print(str(totalFalsePositives / totalIteration) + "/" + str(testSize))