# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

def backspaceCompare(s: str, t: str) -> bool:
    s1, s2 = [], []
    
    for c in s:
        if c != '#':
            s1.append(c)
        elif s1 and c == '#':
            s1.pop()
        
    for c in t:
        if c != '#':
            s2.append(c)
        elif s2 and c == '#':
            s2.pop()
    print(s1, s2)    
    if len(s1) != len(s2):
        return False
    # print(s1, s2)
    
    while s1 and s2:
        if s1.pop() != s2.pop():
            return False
        
    return not s1 and not s2


# s = "ab#c"; t = "ad#c"
# print(backspaceCompare(s, t))

# s = "ab##"; t = "c#d#"
# print(backspaceCompare(s, t))

# s = "a#c"; t = "b"
# print(backspaceCompare(s, t))

s = "y#fo##f"; t = "y#f#o##f"
print(backspaceCompare(s, t))