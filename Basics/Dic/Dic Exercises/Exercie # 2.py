# dow.py

# Open the file
fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

# Create dictionary to store counts
counts = dict()

# Process each line
for line in fhandle:
    # Only process lines that start with "From "
    if line.startswith("From: "):
        words = line.split()
        print("Words",words)
        day = words[2]  # Third word is the day of the week
        counts[day] = counts.get(day, 0) + 1

print(counts)
