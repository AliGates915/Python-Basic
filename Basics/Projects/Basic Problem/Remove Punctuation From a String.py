punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# To take input from the user
my_str =input("Enter a string: ")
# remove punctuation from the string
no_punct =""
for char in my_str:
  if char not in punctuations:
    no_punct = no_punct + char
# display the unpunctuated string
print(no_punct)

# Hello!!!, he said ---and went
# Hello he said and went