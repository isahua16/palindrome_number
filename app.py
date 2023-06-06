num1 = 121
num2 = -121

def palindrome_checker(num):
    forward = str(num)
    reverse = forward[::-1]
    if(forward == reverse):
        return True
    else:
        return False

is_palindrome = palindrome_checker(num1)
print(is_palindrome)
