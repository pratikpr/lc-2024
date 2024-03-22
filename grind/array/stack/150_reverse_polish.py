# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

def evalRPN(tokens) -> int:
    stack = []
    
    for c in tokens:
        try:
            c = int(c)
        except Exception as e:
            pass
        
        if c not in ['+', '-', '*', '/']:
            stack.append(c)
        else:
            if c == '+':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1+op2)
            elif c == '-':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1-op2)
            elif c == '*':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1*op2)
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(op1/op2))
        
    return stack[0]
            
tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))

tokens = ["4","13","5","/","+"]
print(evalRPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))