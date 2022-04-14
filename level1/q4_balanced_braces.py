from collections import deque

def balanced_braces(string):
	st = deque()
	maper = {
		"}": "{",
		"]": "[",
		")": "(",
	}
	all_open_braces = ["{", "[", "("]
	string = "(" + string + ")"
	for ch in string:
		if ch in ["]", "}", ")"]:
			open_brace = maper[ch]
			if len(st) == 0:
				return False
			elif st[-1] == open_brace:
				st.pop()
			else:
				return False
		elif ch in all_open_braces:
			st.append(ch)
	return True if len(st) == 0 else False

if __name__ == "__main__":
	string = "([(a + b) + {(c + d) * (e / f)}]"
	print(balanced_braces(string))
