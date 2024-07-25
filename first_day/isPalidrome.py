#Program to check if a input sentence or number is  palindromic or not
def  isPalindrome(data):
    """check if it is a numebr or sentence
            if number then compare with the reversed string
            If sentence, make it lowercase(or Uppercase), delete all ',' and ' '(white spaces)
    """
    new_data = data
    if not data.isdecimal():
        # this is a sentence
        data = data.lower()
        new_data = ""
        for ch in data:
            if ch.isalnum():
                new_data += ch
    return new_data == new_data[::-1]


# Driver code [Must Include]
while True:
    data = input("Enter number or some sentence: ")
    if not data:
        print("EXITING....")
        break
    print(isPalindrome(data))
        
