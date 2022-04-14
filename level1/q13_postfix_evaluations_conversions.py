from collections import deque


def postfix(exp):

	value_st = deque()
	prefix_st = deque()
	infix_st = deque()
	for ch in exp:
		print("value",value_st)
		print("prefix",prefix_st)
		print("infix",infix_st)
		if ch in ["+", "-", "*", "/"]:
			
			# value stack
			v2 = value_st.pop()
			v1 = value_st.pop()
			if ch == '+':
				value = int(v1) + int(v2)
			elif ch == '-':
				value = int(v1) - int(v2)
			elif ch == '*':
				value = int(v1) * int(v2)
			elif ch == '/':
				value = int(v1) / int(v2)
			value_st.append(value)
			
			# prefix stack
			pv2 = prefix_st.pop()
			pv1 = prefix_st.pop()
			pre_exp = ch + pv1 + pv2
			prefix_st.append(pre_exp)

			# infix stack
			iv2 = infix_st.pop()
			iv1 = infix_st.pop()
			in_exp =  "(" + iv1 + ch + iv2 + ")"
			infix_st.append(in_exp)
		else:
			value_st.append(ch)
			prefix_st.append(ch)
			infix_st.append(ch)
	print(value_st[-1])
	print(infix_st[-1])
	print(prefix_st[-1])


if __name__ == "__main__":
	exp = "92+36-/4*8+"
	postfix(exp)