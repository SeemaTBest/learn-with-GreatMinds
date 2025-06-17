# Function to check if two strings are anagrams
# What Are Anagrams?
# An anagram is a word or phrase formed by rearranging the letters of another word or phrase, 
# using all the original letters exactly once.

def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase to ensure uniform comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort the characters and compare
    return sorted(str1) == sorted(str2)

# --- Test Cases ---

# Basic example with lowercase letters
print(is_anagram("silent", "listen"))  # ✅ True

# Example with uppercase letters
print(is_anagram("Triangle", "Integral"))  # ✅ True

# Example with spaces
print(is_anagram("Conversation", "Voices rant on"))  # ✅ True

# Not an anagram
print(is_anagram("hello", "world"))  # ❌ False

# Anagram with repeated characters
print(is_anagram("aabbcc", "abcabc"))  # ✅ True

# Anagram with mixed cases and whitespace
print(is_anagram("School master", "The classroom"))  # ✅ True

# Empty strings
print(is_anagram("", ""))  # ✅ True (trivially anagrams)

# Strings with different lengths
print(is_anagram("abcd", "abc"))  # ❌ False