fname = input("Enter file name : ")
try:
  fHand = open(fname)
except:
  print("File cannot be opened?")
  exit()

counts = dict()
 
for line in fHand:
  print("Line",line)
  words = line.split();
  print("words", words)
  for word in words:
    if word not in counts:
      counts[word] = 1
    else:
      counts[word] += 1

print(counts)