# Write a function that takes a string, s, as an input and determines whether or not it is a palindrome.

def is_palindrome(s):
    l, r = 0, len(s)-1
    
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
        
    return True


s = "hello"
print(is_palindrome(s))

s = "racecar"
print(is_palindrome(s))

s = "A"
print(is_palindrome(s))
