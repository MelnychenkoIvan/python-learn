def anagram_solution1(s1, s2):
    if len(s1) != len(s2):
        return False
    alist = list(s2)

    stillOk = True
    pos1 = 0

    while pos1 < len(s1) and stillOk:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOk = False

        pos1 = pos1 + 1

    return stillOk


def anagram_solution2(s1, s2):
    if len(s1) != len(s2):
        return False

    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


def anagram_solution3(s1, s2):
    if len(s1) != len(s2):
        return False

    sq1 = [0] * 26
    sq2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        sq1[pos] = sq1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        sq2[pos] = sq2[pos] + 1

    j = 0
    still_ok = True

    while j < 26 and still_ok:
        if sq1[j] == sq2[j]:
            j = j + 1
        else:
            still_ok = False

    return still_ok


print(anagram_solution1('python', 'thonpy'))
print(anagram_solution2('python', 'thonpy'))
print(anagram_solution3('python', 'thonpy'))

