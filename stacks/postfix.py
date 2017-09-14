from stacks.stack import Stack


def infix_to_postfix(infix_expr):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    infix_list = infix_expr.split()
    postfix_list = []
    oper = dict()
    oper["*"] = 3
    oper["/"] = 3
    oper["+"] = 2
    oper["-"] = 2
    oper["("] = 1
    op_stack = Stack()

    for token in infix_list:
        if token in alphabet:
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        elif token in oper:
            while not op_stack.is_empty() and oper[op_stack.peek()] >= oper[token]:
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)


def count_postfix(postfix_expr):
    alphabet = '0123456789'
    op_stack = Stack()

    for token in postfix_expr:
        if token in alphabet:
            op_stack.push(int(token))
        elif token in "*/+-":
            op1 = op_stack.pop()
            op2 = op_stack.pop()
            res = do_math(token, op1, op2)
            op_stack.push(res)

    return op_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2


print(infix_to_postfix("( A + B ) * C"))
print(infix_to_postfix("A + B * C"))
print(infix_to_postfix("( 6 + 3 ) * ( 2 + 1 )"))
print(count_postfix(infix_to_postfix("( 1 + 1 ) * ( 1 + 1 )")))