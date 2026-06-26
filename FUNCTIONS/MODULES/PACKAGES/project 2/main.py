
import mymodule

name = input("Enter name: ")

# Palindrome check
print(mymodule.ispalindrome(name))

# Vowel count
print("No of vowels:", mymodule.count_the_vowels(name))

# Frequency count
freq = mymodule.frequency_of_letters(name)

print("Frequency of letters:", end=" ")
for key, value in freq.items():
    print(f"{key}-{value}", end=" ")
