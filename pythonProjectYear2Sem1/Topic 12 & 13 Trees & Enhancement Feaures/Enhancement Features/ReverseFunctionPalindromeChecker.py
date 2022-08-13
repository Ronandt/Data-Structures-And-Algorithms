

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