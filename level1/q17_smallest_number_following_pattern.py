from collections import deque

def sol(string):
	counter = 1
	st = deque()
	ans = ""
	for ch in string:
		st.append(counter)
		counter += 1
		if ch == "i":
			while len(st):
				top = st.pop()
				ans = ans + str(top)
	st.append(counter)
	while len(st):
		top = st.pop()
		ans = ans + str(top)
	return ans

if __name__ == '__main__':
	string = "ddddiiii"
	print(sol(string))
