import array as array


# Define palindrome and use reverse string function/
def Palindrome(str):
    Palicheck = ''.join(reversed(Word))

    if (str == Palicheck):
        return True
    return False


# Main program
Word = input("Input a word that is a Palindrome ")
answer = Palindrome(Word)

if (answer):
    print("Yes, your word is a Palindrome!")
else:
    print("No, unfortunately that word is not a Palindrome")