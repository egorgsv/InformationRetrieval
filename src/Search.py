import sys


def OR(x: list, y: list) -> list:
    i = 0
    j = 0
    ans = []
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            ans.append(x[i])
            i += 1
        elif x[i] > y[j]:
            ans.append(y[j])
            j += 1
        elif x[i] == y[j]:
            ans.append(x[i])
            i += 1
            j += 1
    return ans


def AND(x: list, y: list) -> list:
    i = 0
    j = 0
    ans = []
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            i += 1
        elif x[i] > y[j]:
            j += 1
        elif x[i] == y[j]:
            ans.append(x[i])
            i += 1
            j += 1
    return ans


def NOT(x: list, docs_count: int) -> list:
    ans = []
    for i in range(docs_count):
        if i not in x:
            ans.append(i)


OPERATORS = {
    'OR', 'NOT', 'AND'
}


def search(expr: list, docs_count: int) -> list:
    stack = []

    for atom in expr:
        if type(atom) is list:
            stack.append(atom)
        else:
            if atom == "AND":
                oper2 = stack.pop()
                oper1 = stack.pop()
                oper = AND(oper1, oper2)
            elif atom == "OR":
                oper2 = stack.pop()
                oper1 = stack.pop()
                oper = OR(oper1, oper2)
            elif atom == "NOT":
                oper = stack.pop()
                oper = NOT(oper, docs_count=docs_count)
            stack.append(oper)

    return stack
