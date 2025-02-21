def findDog(str):
  return 'dog' in str.lower().split()


print(findDog("This is dog is here"))

# Count Number of Dogs
def countDog(s):
  count = 0;
  for word in s.lower().split():
    if word == 'dog':
      count += 1
  return count

print(countDog("Dog is barking, when another dog is seeing the another dog"))
