def BinaryTree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])


def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])


def get_root(t):
    return t[0]


def get_left(t):
    return t[1]


def get_right(t):
    return t[2]


t = BinaryTree('a')
insert_left(t, 'b')
insert_right(get_left(t), 'd')

insert_right(t, 'c')
insert_left(get_right(t), 'e')
insert_right(get_right(t), 'f')
print('t: {}'.format(t))
