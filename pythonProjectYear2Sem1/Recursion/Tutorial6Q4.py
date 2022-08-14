def isPalindrome(aStr):
    if len(aStr) < 2:
        return True
    # elif aStr[0] != aStr[-1]:
    #     return False
    return aStr[0] == aStr[-1] and isPalindrome(aStr[1:-1])

print(isPalindrome('level'))
print("level"[1:-1])
print("madam"[1:-1])
print("ada"[1:-1])
while True:
    aStr = input("Enter a string (q to quit): ")
    aStr = aStr.lower()

    if aStr == 'q':
        break

    aStr = ''.join(ch for ch in aStr if ch.isalnum())

    is_a_palindrome = isPalindrome(aStr)

    if is_a_palindrome:
        print("'{}' is a palindrome.".format(aStr))
    else:
            print("'{}' is not a palindrome.".format(aStr))
