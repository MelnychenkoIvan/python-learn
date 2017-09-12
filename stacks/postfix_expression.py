from stacks.stack import Stack


def infix_to_postfix(infixexpr):
    prec = dict()
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    token_list = infixexpr.split()
    postfix_list = []
    opstack = Stack()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            opstack.push(token)

    print(postfix_list)

infix_to_postfix("( A + B ) * C")
