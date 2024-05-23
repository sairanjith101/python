
def palindrome_string(word):

    text = ''.join(reversed(word))
    
    if text == word:
        return 1
    else:
        return 0

S = "abba"
# S = "abc"
# S = "deified"
print(palindrome_string(S))