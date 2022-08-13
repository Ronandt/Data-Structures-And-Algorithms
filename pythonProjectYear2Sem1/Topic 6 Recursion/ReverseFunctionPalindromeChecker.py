# Improvement:
# Checking If String is a Palindrome with a reverse Function
#
# Python enables us to use the reverse function. We know intuitively that a word read forwards and backwards, if same is a palindrome.
# Hence, let us generate the forward and backward string for the same, and check if the two strings are the same.
#
# Link:https://www.mygreatlearning.com/blog/palindrome-in-python/#reverse-function

def check_palindrome_1(string):
    reversed_string = string[::-1]
    status=1
    if(string!=reversed_string):
        status=0
    return status


string = ''
while string != "q":
    string = input("Enter the string(Enter q to quit): ").lower()
    status= check_palindrome_1(string)
    if(status):
        print(string,"is a palindrome ")
        continue
    else:
        print(string,"is not a palindrome ")
        continue