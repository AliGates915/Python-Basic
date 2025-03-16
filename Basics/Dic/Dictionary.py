word = 'hello'
d = dict()
for c in word:
  if c not in d:
    d[c] = 1
  else:
    d[c] = d[c] + 1

print(d)

# We use  
person = {
  "name" : 'Ali',
  "age"  : 22
}

print(person['name'])
print(person['age'])


# get method automatically handle, where key is not in a dictionary.
# word = 'hello'
# d = dict()
# for c in word:
#    d[c] = d.get(c,0) + 1

# print(d)
