from stacks.stack import Stack


def infix_to_postfix(infix_expr):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    postfix_list = []
    oper = dict()
    oper["*"] = 3
    oper["/"] = 3
    oper["+"] = 2
    oper["-"] = 2
    oper["("] = 1
    op_stack = Stack()

    for token in infix_expr:
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


print(infix_to_postfix("(A+ B)*(C+D)"))
print(infix_to_postfix("( A + B ) * C"))
print(infix_to_postfix("A + B * C"))
