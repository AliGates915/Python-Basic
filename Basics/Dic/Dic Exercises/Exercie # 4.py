# exercise4.py

fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

counts = {}

for line in fhandle:
    if line.startswith("From: "):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

max_count = None
max_email = None

for email, count in counts.items():
    if max_count is None or count > max_count:
        max_count = count
        max_email = email

print(max_email, max_count)


# counts.items() means we are getting a list of tuples where each tuple contains a key-value pair from the dictionary like this:
'''
counts = {
    'cwen@iupui.edu': 5,
    'zqian@umich.edu': 3,
    'gsilver@umich.edu': 7
}

'''
