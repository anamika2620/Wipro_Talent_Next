
import sys

# command line arguments
str1 = sys.argv[1].split("-")
str2 = sys.argv[2].split("-")
str3 = sys.argv[3].split("-")

happiness = 0

for num in str3:
    if num in str1:
        happiness += 1
    elif num in str2:
        happiness -= 1

print(happiness)
