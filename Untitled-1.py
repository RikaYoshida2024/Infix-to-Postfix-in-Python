def is_operand(ch):
    return ch.isalpha() or ch.isdigit()
def precedence(op):
    if op=='+' or op=='-':
        return 1
    elif op=='*' or op=='/':
        return 2
    else:
        return 0
def infix_to_postfix(expression):
    stack=[]
    result=[]
    for char in expression:
        if is_operand(char):
            result.append(char)
        elif char==')':
            while stack and stack[-1]!= '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while (stack and precedence(stack[-1])>=precedence(char)):
                result.append(stack.pop())
            stack.append(char)
    while stack:
        result.append(stack.pop())
    return ''.join(result)
if __name__=='__main__':
    expression = "(a+b)*(c-d)"
    postfix_expression = infix_to_postfix(expression)
    print("The postfix expression is:", postfix_expression)