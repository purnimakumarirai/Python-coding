def isPalindrome( a ):

    return a == a[::-1]

s = "abc"

b = isPalindrome(s)

if b:
    print("Yes")
else:
    print("No")
