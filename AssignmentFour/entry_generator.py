n = 10000000

f = open("sample.txt","w+")
for i in range(n):
     f.write("%d\n" % (i))
f.close() 