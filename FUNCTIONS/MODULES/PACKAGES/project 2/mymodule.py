
def ispalindrome(name):
    if name == name[::-1]:
        return "Yes it is a palindrome."
    else:
        return "No it is not a palindrome."


def count_the_vowels(name):
    count = 0
    vowels = "aeiouAEIOU"

    for ch in name:
        if ch in vowels:
            count += 1

    return count


def frequency_of_letters(name):
    freq = {}

    for ch in name:
        if ch != " ":   # ignore spaces
            freq[ch] = freq.get(ch, 0) + 1

    return freq
