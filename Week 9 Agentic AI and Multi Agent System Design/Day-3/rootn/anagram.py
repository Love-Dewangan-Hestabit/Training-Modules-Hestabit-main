def is_anagram(str1, str2):
    # Remove spaces and convert to lower case
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if sorted strings are equal
    return sorted(str1) == sorted(str2)

# Test the function
print(is_anagram("Listen", "Silent"))  # Expected output: True
print(is_anagram("Hello", "World"))  # Expected output: False