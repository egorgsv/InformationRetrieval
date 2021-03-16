import sys


def reversed_polish_notation(s):
    lex = parse(s)
    s2 = []
    r = []
    oper = ["OR", "AND", "NOT", "(", ")"]
    for a in lex:
        if a == "(":
            s2 = [a] + s2
        elif a in oper:
            if s2 == []:
                s2 = [a]
            elif a == ")":
                while (True):
                    q = s2[0]
                    s2 = s2[1:]
                    if q == "(":
                        break
                    r += [q]
            elif prty(s2[0]) < prty(a):
                s2 = [a] + s2
            else:
                while (True):
                    if s2 == []:
                        break
                    q = s2[0]
                    r += [q]
                    s2 = s2[1:]
                    if prty(q) == prty(a):
                        break
                s2 = [a] + s2
        else:
            r += [a]
    while (s2 != []):
        q = s2[0]
        r += [q]
        s2 = s2[1:]
    return r


def prty(o):
    if o == "OR":
        return 1
    elif o == "AND" or o == "NOT":
        return 2
    elif o == "(":
        return 0


def parse(s):
    lex = []
    for a in s.split():
        if "(" in a:
            lex += ["("] + [a.replace('(', "")]
        elif ")" in a:
            lex += [a.replace(')', "")] + [")"]
        else:
            lex += [a]
    return lex


OPERATORS = {
    '+': float.__add__,
    '-': float.__sub__,
    '*': float.__mul__,
    '/': float.__div__,
    '%': float.__mod__,
    '^': float.__pow__,
}


def search(expr):
    ops = OPERATORS.keys()
    stack = []

    for atom in expr:
        try:
            atom = float(atom)
            stack.append(atom)
        except ValueError:
            for oper in atom:
                if oper not in ops:
                    continue
                try:
                    oper2 = stack.pop()
                    oper1 = stack.pop()
                except IndexError:
                    sys.stderr.write(u"Маловато операндов")
                    sys.exit(1)

                try:
                    oper = OPERATORS[oper](oper1, oper2)
                except ZeroDivisionError:
                    sys.stderr.write(u"Нельзя делить на 0")
                    sys.exit(1)

                stack.append(oper)

    if len(stack) != 1:
        sys.stderr.write(u"Многовато операндов")
        sys.exit(1)

    return stack.pop()
