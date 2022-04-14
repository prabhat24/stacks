from collections import deque

def sol(arr):
	N = len(arr)
	st = deque()
	ans = [0] * N
	for i, num in enumerate(arr):
		while len(st) and num > arr[st[-1]]:
			st.pop()
		if len(st):
			getl = st[-1]
		else:
			getl = -1
		ans[i] = i - getl
		st.append(i)
		print("st", st, "ans", ans)
	return ans

if __name__ == "__main__":
	arr = [2, 5, 9, 3, 1, 12, 6, 8, 7]
	print(sol(arr))