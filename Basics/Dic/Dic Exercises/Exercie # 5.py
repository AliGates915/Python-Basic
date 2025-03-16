# exercise5.py

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
        domain = email.split('@')[1]
        counts[domain] = counts.get(domain, 0) + 1

print(counts)
