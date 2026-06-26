
# open file
file = open("sample.txt", "r")

lines = file.readlines()

# count number of lines
n = len(lines)

# meeting time
if n <= 12:
    print("Meeting time:", n, "AM")
else:
    print("Meeting time:", n - 12, "PM")

# count word frequency
freq = {}

for line in lines:
    words = line.split()
    for word in words:
        word = word.strip(".,!?").lower()   # remove punctuation
        freq[word] = freq.get(word, 0) + 1

# find max repeated word
max_word = max(freq, key=freq.get)

print("Meeting place:", max_word.capitalize(), "Street")

file.close()
