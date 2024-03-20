# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

def calculate(s: str) -> int:
    stack = []
    curr, op = 0, '+'
    
    i = 0
    while i < len(s):
        c = s[i]
        
        if c.isalnum():
            curr = curr*10 + int(c)
        if not c.isalnum() and c != ' ' or i == len(s)-1:
            if op == '+':
                stack.append(curr)
            elif op == '-':
                stack.append(-1 * curr)
            elif op == '*':
                stack.append(stack.pop() * curr)
            else:
                if stack[-1] < 0:
                    num = -1 * stack.pop()
                    stack.append(-1 * (num//curr))
                else:
                    stack.append(stack.pop() // curr)
            op = c
            curr = 0
        i += 1

                
    return sum(stack)

s = "14-3/2"
print(calculate(s))

s = " 42 "
print(calculate(s))

s = " 3+5 / 2 "
print(calculate(s))
                