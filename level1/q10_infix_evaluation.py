from collections import deque

def check_pri(ope1, ope2):
    # return true if ope1 has higher priority than ope2
    if ope1 in ["/", "*"]:
        return True
    if ope2 in ["+", "-"] and ope1 in ["+", "-", "/", "*"]:
        return True
    elif ope2 in ["*", "/"] and ope1 in ["+", "-"]:
        return False
    else:
        return False

def infix(exp):
    value_stack = deque()
    operator_stack = deque()
    for ch in exp:
        if ch in ["1","2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            value_stack.append(ch)
        elif ch == "(":
            operator_stack.append(ch)
        elif ch in ["+", "-", "/", "*"]:
            while len(operator_stack) and check_pri(operator_stack[-1], ch):
                top_operator_stack = operator_stack.pop()
                o2 = value_stack.pop()
                o1 = value_stack.pop()
                if top_operator_stack == "+":
                    value_stack.append(int(o1) + int(o2))
                elif top_operator_stack == "-":
                    value_stack.append(int(o1) - int(o2))
                elif top_operator_stack == "*":
                    value_stack.append(int(o1) * int(o2))
                elif top_operator_stack == "/":
                    value_stack.append(int(o1) // int(o2))
            operator_stack.append(ch)
        elif ch == ")":
            while len(operator_stack) and operator_stack[-1] != "(":
                top_operator_stack = operator_stack.pop()
                o2 = value_stack.pop()
                o1 = value_stack.pop()
                if top_operator_stack == "+":
                    value_stack.append(int(o1) + int(o2))
                elif top_operator_stack == "-":
                    value_stack.append(int(o1) - int(o2))
                elif top_operator_stack == "*":
                    value_stack.append(int(o1) * int(o2))
                elif top_operator_stack == "/":
                    value_stack.append(int(o1) // int(o2))

            if len(operator_stack) and operator_stack[-1] == "(":
                operator_stack.pop()
    print(operator_stack)
    print(value_stack)
    while len(operator_stack):
        top_operator_stack = operator_stack.pop()
        o2 = value_stack.pop()
        o1 = value_stack.pop()
        if top_operator_stack == "+":
            value_stack.append(int(o1) + int(o2))
        elif top_operator_stack == "-":
            value_stack.append(int(o1) - int(o2))
        elif top_operator_stack == "*":
            value_stack.append(int(o1) * int(o2))
        elif top_operator_stack == "/":
            value_stack.append(int(o1) // int(o2))
    return value_stack[-1]

if __name__ == "__main__":
    exp = "3/(6*8-4)+9"
    # exp = "(6*8-4)"
    print(infix(exp))

