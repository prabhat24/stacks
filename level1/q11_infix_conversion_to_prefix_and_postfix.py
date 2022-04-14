
# algorithm
# 0. add close brace at the end of the string expression & add open brack to the top of the stack
# 1. itterate over the expression. maintain 2 stack operator and orerand. 
# 2. if ( is encountered push it to operator stack.
# 3. if operands are encountered push it to operand stack.
# 4. if operator: 
# 		pop all the operators which have precedance >= the operator
# 5. if closing brace  ):
#		then pop all the operators and simultaneously complete postfix/ prefix notations on operand stack

from collections import deque

def have_higher_p(op1, ch):
	# returns true if ope1 has higher or equal precedance than ch
	if op1 in ["*", "/"]:
		return True
	elif ch in ["+", "-"] and op1 in ["+", "-", "/", "*"]:
		return True
	elif ch in ["*", "/"] and op1 in ["+", "-"]:
		return False
	else: 
		return False


def infix(arr, n, make):

	p_stack = deque()
	value_stack = deque()

	p_stack.append("(")
	arr = arr + ")"

	for ch in arr:
		if ch  == "(":
			p_stack.append(ch)
		elif ch in ["+", "-", "*", "/"]:
			while len(p_stack) and have_higher_p(p_stack[-1], ch):
				v2 = value_stack.pop()
				v1 = value_stack.pop()
				ope = p_stack.pop()
				if make == "postfix":
					ans = v1 + v2 + ope
					value_stack.append(ans)
				else:
					ans = ope + v1 + v2
					value_stack.append(ans)
			p_stack.append(ch)
		elif ch == ")":
			while len(p_stack) and p_stack[-1] != "(":
				v2 = value_stack.pop()
				v1 = value_stack.pop()
				ope = p_stack.pop()
				if make == "postfix":
					ans = v1 + v2 + ope
					value_stack.append(ans)
				else:
					ans = ope + v1 + v2
					value_stack.append(ans)
			if len(p_stack) and p_stack[-1] == "(":
				p_stack.pop()
		else:
			value_stack.append(ch)
	return value_stack[-1]


if __name__ == '__main__':
	arr = "a*(b-c+d)/e"
	print(infix(arr, len(arr), make="prefix"))
	print(infix(arr, len(arr), make="postfix"))
