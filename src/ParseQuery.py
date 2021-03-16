from nltk.corpus import stopwords


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
        if a in stopwords("english"):
            continue
        if "(" in a:
            lex += ["("] + [a.replace('(', "")]
        elif ")" in a:
            lex += [a.replace(')', "")] + [")"]
        else:
            lex += [a]
    return lex