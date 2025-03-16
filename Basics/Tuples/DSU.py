# Decorate Sort Undecorate

txt = "but soft what light in windows breaks"
words = txt.split()
t = list()

for word in words:
  # count the len of the word and append like window have 6 letters and in have 2 letters, so append 6 in the t.
  t.append((len(word),word))
  # print(t.append((len(word),word)))

t.sort(reverse=True)
res = list()

for length, word in t:
  res.append(word)
print(res)

