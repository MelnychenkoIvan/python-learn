from stacks.stack import Stack

s = 'qwerty'


def revstring(s):
    """String reverse"""

    st = Stack()
    rev_s = ""

    for i in range(len(s)):
        st.push(s[i])

    while not st.is_empty():
        rev_s += st.pop()

    return rev_s


def parChecker(symbolString):
    """Checking the balance of brackets"""

    s = Stack()
    index = 0
    balanced = True

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]

        if symbol in "{[(":
            s.push(symbolString[index])
        elif symbol in "}])":
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(open_s, close_s):
    opens = "([{"
    closers = ")]}"
    return opens.index(open_s) == closers.index(close_s)


def number_converter(decNumber, base=2):
    """Converting number to different number system"""

    digits = "0123456789ABCDEF"
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber //= base

    bin_string = ""
    while not remstack.is_empty():
        bin_string += digits[remstack.pop()]

    return bin_string

print(number_converter(26, base=26))
